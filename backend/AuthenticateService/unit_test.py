import unittest
from main import loadKey, createToken, decodeToken


class AuthenticateServiceTest(unittest.TestCase):
    def test_Does_loadKey_loadkeyFile(self):
        key = loadKey('.key/private.ec.key')
        self.assertNotEqual(key, "")

    def test_Does_CreateToken_generateValidToken(self):
        payload_data = {
            "email": "testmail@mail.com",
            "username": "test"
        }
        key = loadKey('.key/private.ec.key')
        algorithm = 'ES256'
        token = createToken(payload_data, key, algorithm)
        self.assertNotEqual(token, "")
        
        decodedToken = decodeToken(token, key, algorithm)
        self.assertEquals(decodedToken["email"], payload_data["email"])
        self.assertEquals(decodedToken["username"], payload_data["username"])

    def test_Does_decodeToken_DecodeToken(self):
        payload_data = {
            "email": "testmail@mail.com",
            "username": "test"
        }
        key = loadKey('.key/private.ec.key')
        algorithm = 'ES256'
        token = createToken(payload_data, key, algorithm)
        
        decodedToken = decodeToken(token, key, algorithm)
        self.assertNotEqual(decodedToken, "")
        
if __name__ == '__main__':
    unittest.main()