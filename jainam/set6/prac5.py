def checkCommon(l1,l2):
    s3 = set(l1).intersection(set(l2))
    if len(s3)==0:
        return False
    return True
l1=[1,2,3]
l2=[3,4,5]
print(checkCommon(l1,l2))