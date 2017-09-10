import base64, hashlib, hmac

jid = "4917623966428@c.us"
accountJid = "4936758269010@c.us"
cipher = "576861747341707020496d616765204b657973"

digTo = hmac.new(cipher.encode("utf-8"), jid.replace("@s.whatsapp.net", "@c.us").encode("utf-8"),
    hashlib.sha256).digest()[:20]
refTo = base64.b64encode(digTo).decode()
digFrom = hmac.new(cipher.encode("utf-8"), accountJid.replace("@s.whatsapp.net", "@c.us").encode("utf-8"),
    hashlib.sha256).digest()[:20]
refFrom = base64.b64encode(digFrom).decode()
print("  digTo: " + digTo)
print("  refTo: " + refTo)
print("digFrom: " + digFrom)
print("refFrom: " + refFrom)