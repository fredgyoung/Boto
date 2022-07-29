'''
Documentation:


Every object in Amazon S3 can be uniquely addressed through the combination of the web service endpoint,
bucket name, key, and optionally, a version. For example, in the URL
https://DOC-EXAMPLE-BUCKET.s3.us-west-2.amazonaws.com/photos/puppy.jpg,
DOC-EXAMPLE-BUCKET is the name of the bucket and photos/puppy.jpg is the key.

'''

import boto3

BUCKET_NAME = 'fgyacloudguru12345'

class App:
    def __init__(self, bucket_name):
        # self.client = boto3.client('s3')
        self.resource = boto3.resource('s3')
        self.bucket = self.resource.Bucket(bucket_name)
        self.filenames = []

    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html
    def _configure(self):
        pass

    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
    def _credentials(self):
        pass

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects
    def _get_filenames(self):
        response = self.resource.list_objects_v2(Bucket=BUCKET_NAME)
        content_array = response['Contents']
        for item in content_array:
            filename = item['Key']
            self.filenames.append(filename)

    def _rename_file(self):

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.copy_object
    def _copy_file(self):
        response = self.resource.copy_object(
            Bucket=BUCKET_NAME,
            CopySource='string' or {'Bucket': BUCKET_NAME, 'Key': 'string'},
            Key='string',
        )

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_object
    def _delete_file(self):
        response = self.resource.copy_object(
            Bucket=BUCKET_NAME,
            Key='string',
        )

    def run(self):
        self._get_filenames()
        self._copy_file()
        self._delete_file()


if __name__ == '__main__':

    app = App(BUCKET_NAME)
