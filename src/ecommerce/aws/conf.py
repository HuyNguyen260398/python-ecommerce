# import datetime
#
# AWS_GROUP_NAME = "Python_eCommerce_Group"
# AWS_USERNAME = "Admin_Python_eCommerce"
# AWS_ACCESS_KEY_ID = "AKIAQE2WXIOJB3QGBSOQ"
# AWS_SECRET_ACCESS_KEY = "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"
#
# AWS_FILE_EXPIRE = 200
# AWS_PRELOAD_METADATA = True
# AWS_QUERYSTRING_AUTH = True
#
# DEFAULT_FILE_STORAGE = 'ecommerce.aws.utils.MediaRootS3BotoStorage'
# STATICFILES_STORAGE = 'ecommerce.aws.utils.StaticRootS3BotoStorage'
# AWS_STORAGE_BUCKET_NAME = '<your_bucket_name>'
# S3DIRECT_REGION = 'us-west-2'
# S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_ROOT = MEDIA_URL
# STATIC_URL = S3_URL + 'static/'
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
#
# two_months = datetime.timedelta(days=61)
# date_two_months_later = datetime.date.today() + two_months
# expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")
#
# AWS_HEADERS = {
#     'Expires': expires,
#     'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
# }

# AWS_STORAGE_BUCKET_NAME = '<your-aws-bucket-name>'
# AWS_ACCESS_KEY_ID = '<your-aws-user-access-key-id>'
# AWS_SECRET_ACCESS_KEY =  '<your-aws-user-secret-key>'
#
# S3DIRECT_REGION =  'us-west-2'
#
# PROTECTED_DIR_NAME = '<your-in-bucket-dir-name>'
# PROTECTED_MEDIA_URL = '//%s.s3.amazonaws.com/%s/' %( AWS_STORAGE_BUCKET_NAME, PROTECTED_DIR_NAME)
#
# AWS_DOWNLOAD_EXPIRE = 5000 #(0ptional, in milliseconds)
