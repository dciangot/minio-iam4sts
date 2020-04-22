from minio import Minio
import requests
import xmltodict

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImJhZWM3ZDZkNjk0OGM4YjFmMDQxM2M4MWE5NmIzODEwNWE2MTMzYzMifQ.eyJpc3MiOiJodHRwOi8vOTAuMTQ3LjE3NC45Mjo1NTU2L2RleCIsInN1YiI6IkNpUTBOelkyTkRKa055MHhaRFJpTFRSbU56Y3RPRGN5TlMxbFl6aGhNMlExTkRjME5qTVNCV1J2WkdGeiIsImF1ZCI6Im1pbmlvLWNuYWYiLCJleHAiOjE1ODc2NTg5MDgsImlhdCI6MTU4NzU3MjUwOCwibm9uY2UiOiJBOWxvT3dzUTN5ZDY0c1VGIiwiYXRfaGFzaCI6Il9RVG9aeVhVNWJKVGtSc1FKUjJIckEiLCJlbWFpbCI6IkRhbmllbGUuU3BpZ2FAcGcuaW5mbi5pdCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiRGFuaWVsZSBTcGlnYSJ9.ZmYNiV0peKOAnk08HqeKaYyYUmooNxk2HZQgkVMLtJ22lxRD3oqGz4gP2mMhkftRn5BX0bAATF3tSZIGmZoI7RKhN-izWspUx-fwhLEFg2PhvXzxRx9HXa7nmkhx3a8aZJERqeZj_ETqp_S_ziqiIASx8-UHG6BTXWJZX4u8AGsLrJRqyXcKdFU-LAYdARgae64yR1QL8zeCnHf_vuqNf-91YIpCWdYGCWRdlTCwxP5E53JgSn1oGSC-nPr6_Ddlg8hPbjxcE9FJMlhnKSuXPnfUlZC78fwh-RAjCMtBf7lyJlu1ZMEaR6ofj1YcvcEXkP6I3lbFgR4wcNCgm_L87A"

r = requests.post("http://131.154.97.121:9000", data={
    'Action': "AssumeRoleWithWebIdentity",
    'Version': "2011-06-15",
    'WebIdentityToken': token
})

print(r.status_code, r.reason)

tree = xmltodict.parse(r.content)

credenstials = dict(tree['AssumeRoleWithWebIdentityResponse']['AssumeRoleWithWebIdentityResult']['Credentials']).keys()
# [u'SecretAccessKey', u'AccessKeyId', u'Expiration', u'SessionToken']

