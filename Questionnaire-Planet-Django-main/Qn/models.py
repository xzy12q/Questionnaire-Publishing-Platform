from django.db import models
from userinfo.models import *
# 在此处创建模型。

def question_image_directory_path(instance, filename):
    # 文件上传到 MEDIA_ROOT/image/question_<id>/<filename>目录中
    return 'image/question_{0}/{1}'.format(instance.question_id, filename)


def question_video_directory_path(instance, filename):
    # 文件上传到 MEDIA_ROOT/video/question_<id>/<filename>目录中
    return 'video/question_{0}/{1}'.format(instance.question_id, filename)

class Survey(models.Model):
    survey_id = models.AutoField(primary_key=True,verbose_name="id")
    title = models.CharField(max_length=50,verbose_name="标题")
    description = models.CharField(max_length=256,verbose_name="简介",blank=True)
    # password = models.CharField(max_length=64,blank=True,)

    question_num = models.PositiveIntegerField(default=0,verbose_name="题目数目") # 非负整数
    recycling_num = models.PositiveIntegerField(default=0,verbose_name="回收数目")
    max_recycling = models.PositiveIntegerField(default=999999,verbose_name="最大回收数目")

    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    release_time = models.DateTimeField(verbose_name="发布时间",null=True)
    finished_time = models.DateTimeField(verbose_name="结束时间",null=True)

    is_released = models.BooleanField(default=False,verbose_name="是否已发行")
    is_deleted = models.BooleanField(default=False,verbose_name="是否已删除")
    is_collected = models.BooleanField(default=False, verbose_name="是否被收藏")
    is_finished = models.BooleanField(default=False, verbose_name="是否已结束")
    # is_encrypted_pin = models.BooleanField(default=False)

    username = models.CharField(max_length=128, verbose_name="用户名")

    share_url = models.URLField(verbose_name="分享链接",default='')
    docx_url = models.URLField(verbose_name="word链接",default='')
    pdf_url = models.URLField(verbose_name="pdf链接", default='')
    excel_url = models.URLField(verbose_name="答卷数据统计excel链接",default='')

    SURVEY_TYPE_CHOICES = [
        (1,'普通问卷'),
        (2,'考试问卷'),
        (4,'投票问卷'),
        (3,'报名问卷'),
    ]
    type = models.CharField(max_length=32, verbose_name="问卷类型",default='')
    is_logic = models.BooleanField(default=False,verbose_name="是否存在逻辑问题")


class Question(models.Model):

    question_id = models.AutoField(primary_key=True,verbose_name="问题id")
    title = models.CharField(max_length=64,verbose_name="标题",blank=True,default='默认标题')
    direction = models.CharField(max_length=256,blank=True,verbose_name="说明")
    is_must_answer = models.BooleanField(default=False,verbose_name="是必答题")

    survey_id = models.ForeignKey(Survey,on_delete=models.CASCADE,verbose_name="所属问卷id")
    sequence = models.IntegerField(default=0,verbose_name="题目顺序")
    option_num = models.PositiveIntegerField(default=0,verbose_name="选项数目")

    score = models.PositiveIntegerField(default=0,verbose_name="打分最高分")
    raw = models.PositiveIntegerField(default=1, verbose_name="行数")
    point = models.PositiveIntegerField(default=0,verbose_name="问题得分")
    TYPE_CHOICES = [
        (0, '单选'),
        (1, '多选'),
        (2, '填空'),
        (3, '评分'),
    ]
    # type = models.IntegerField(choices=TYPE_CHOICES,default=0,verbose_name="题型")
    type = models.CharField(max_length=256,verbose_name="问题类型",default='radio')
    right_answer = models.CharField(max_length=256,verbose_name="正确答案",default='')

    isVote = models.BooleanField(default=False, verbose_name="是投票题")

    has_image = models.BooleanField(default=False, verbose_name="包含图片")
    has_video = models.BooleanField(default=False, verbose_name="包含视频")
    image_url = models.CharField(max_length=1024,verbose_name="图片链接",blank=True,default='')
    # image = models.ImageField(upload_to=question_image_directory_path, blank=True, verbose_name="图片文件")
    video_url = models.CharField(max_length=1024,verbose_name="视频链接",blank=True,default='')
    # video = models.FileField(upload_to=question_video_directory_path, blank=True, verbose_name="视频文件")

    # last_option = models.ForeignKey(Option,on_delete=models.CASCADE,verbose_name="上一个选项")
    last_option = models.IntegerField(default=0, verbose_name="上一个选项")
    last_question = models.IntegerField(default=0, verbose_name="上一个问题")
    is_shown = models.BooleanField(default=True, verbose_name="展示题目")

    # radio checkbox 单选题 多选题 text 填空 mark 判断 location 定位
class Option(models.Model):

    option_id = models.AutoField(primary_key=True,verbose_name="选项编号")
    order = models.PositiveIntegerField(default=1,verbose_name="选项位置")
    #从1递增
    content = models.CharField(max_length=128,verbose_name="内容")
    question_id  = models.ForeignKey(Question, on_delete=models.CASCADE,verbose_name="问题编号")
    num_limit = models.PositiveIntegerField(default=0,verbose_name="最大额度")
    remain_num = models.PositiveIntegerField(default=0,verbose_name="剩余额度")
    has_num_limit = models.BooleanField(default=False, verbose_name="是否有额度限制")


class Submit(models.Model):
    submit_id = models.AutoField(primary_key=True,verbose_name="提交编号")
    survey_id = models.ForeignKey(Survey,on_delete=models.CASCADE,verbose_name="问卷编号")
    submit_time = models.DateTimeField(auto_now_add=True,verbose_name="提交时间")
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="用户编号")
    username = models.CharField(max_length=128,blank=True,verbose_name="用户名")

    is_valid = models.BooleanField(default=True,verbose_name="答卷是否有效")
    score = models.PositiveIntegerField(default=0,verbose_name="答卷总得分")

class Answer(models.Model):

    answer_id = models.AutoField(primary_key=True,verbose_name="回答编号")
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE,verbose_name="问题编号")
    submit_id = models.ForeignKey(Submit, on_delete=models.CASCADE,verbose_name="提交编号")
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="用户编号")
    answer = models.CharField(max_length=128,verbose_name="答案")
    score = models.PositiveIntegerField(default=0, verbose_name="单题得分")

    username = models.CharField(max_length=128, blank=True, verbose_name="用户名")
    TYPE_CHOICES = [
        (0, '单选'),
        (1, '多选'),
        (2, '填空'),
        (3, '评分'),
    ]
    # type = models.IntegerField(choices=TYPE_CHOICES, default=0,verbose_name="题目类型")
    type = models.CharField(max_length=32, verbose_name="问题类型",default='')


