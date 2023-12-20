import hashlib


def hash_code(s, salt='Qn'):  # 生成 s+salt 成hash_code（默认：salt=online publish）
    h = hashlib.sha256()
    s += salt
    h.update(s.encode()) # 更新方法 get bytes（type）
    return h.hexdigest()
