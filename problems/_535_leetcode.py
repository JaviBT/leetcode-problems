# 535. Encode and Decode TinyURL
# https://leetcode.com/problems/encode-and-decode-tinyurl

# Solution by: Javi Barranco

# Problem:
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Example 1:
# Input: "https://leetcode.com/problems/design-tinyurl"
# Output: "http://tinyurl.com/4e9iAk"

class Codec:
    def __init__(self):
        self.counter = 0
        self.encodeDic = {}
        self.decodeDic = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.decodeDic[str(self.counter)] = longUrl
        self.encodeDic[longUrl] = str(self.counter)
        self.counter += 1
        return 'https://tinyurl/' + self.encodeDic[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.split('https://tinyurl/')[1]
        return self.decodeDic[shortUrl]
    

exercise = Codec()

input = "https://leetcode.com/problems/design-tinyurl"

expected_output = input

output = exercise.decode(exercise.encode(input))
print(output)
assert output == input, "Wrong answer"
print("Accepted")