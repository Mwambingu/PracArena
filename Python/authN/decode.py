#!/usr/bin/env python3

import base64

encoded_str = base64.b64encode(b'I am encoded!!')

print(encoded_str)

decoded_str = base64.b64decode(encoded_str)

print(decoded_str)