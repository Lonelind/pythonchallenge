from string import maketrans

st = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
ina = "abcdefghijklmnopqrstuvwxyz"
oua = "cdefghijklmnopqrstuvwxyzab"
m = "map"
trantab = maketrans(ina,oua)
print m.translate(trantab)
