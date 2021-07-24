
#
#时间线对象，每个对象包含了信息和唯一ID
#
class SearchParamter:

    def __init__(self, offset, limit, sort, token):
        self.offset = offset
        self.limit = limit
        self.sort = sort
        self.token = token