
#Remove public read right for all S3 Objects and keys within bucket

import sys
import boto3


s3 = boto3.client('s3')
s3rss = boto3.resource('s3')

for bucket in s3rss.buckets.all():
    count = 0
    print "*** Begin bucket {0} ***".format(bucket.name)
    print bucket.name
    #s3tags = s3rss.BucketTagging(bucket.name)
    #if s3tags.tag_set:
    #    print s3tags.tag_set
    #s3 = boto3.resource('s3')


    result = s3.get_bucket_acl(Bucket= str(bucket.name))
    result3 = s3rss.Bucket(str(bucket.name))
    #print result3.objects.all()

    result2 = s3rss.BucketAcl(str(bucket.name))
    acls = result2.grants
    owner =  result2.owner
    list_of_resources = result2.get_available_subresources()
    print list_of_resources
    #get_available_subresources()

    print acls
    new_grants = []
    for grant in result['Grants']:
        if grant['Grantee']['Type'] != "Group":
            new_grants.append(grant)
        elif grant['Grantee']['URI'] != "http://acs.amazonaws.com/groups/global/AllUsers":
            new_grants.append(grant)
        else:
            count += 1


    print new_grants
    if count > 0:
        response2 = result2.put(AccessControlPolicy= { 'Grants': new_grants, 'Owner': owner})
        print response2
        for file in result3.objects.all():
            print file.key
            object_acl = s3rss.ObjectAcl(str(bucket.name),str(file.key))
            object_acl.put(AccessControlPolicy= { 'Grants': new_grants, 'Owner': object_acl.owner})

    print "\nNext bucket*** \n\n"
