class Log:
    def __init__(self, ip, created_at, gmt, request, adress, http, code, bytes_q):
        self._ip = ip
        self._created_at = created_at
        self._gmt = gmt
        self._request = request
        self._adress = adress
        self._http = http
        self._code = code
        self._bytes = bytes_q

    def insert_request(self):
        return "INSERT INTO logs(ip, created_at, gmt, request, adress, http, code, bytes) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', {}, {})".format(
            self._ip, self._created_at, self._gmt, self._request, self._adress, self._http, self._code, self._bytes
        )