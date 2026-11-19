import contextlib
import io
import unittest

import ext


class TestResourcesArn(unittest.TestCase):
    valid = [
        "arn:aws:s3:::noaa-ufs-gefsv13replay-pds",
        "arn:aws:s3:::amp-ad-diverse-cohorts.opendata.sagebase.org",
        "arn:aws:s3:::deafrica-sentinel-5p-co/Sentinel-5p/TROPOMI/TROPO_L2_CO/",
        "arn:aws:s3:::assetdata-igp/Coal Plants/",
        "arn:aws-iso:s3:::some-bucket",
        "arn:aws:sns:us-east-1:123456789012:noaa-gfs-bdp-pds-data-available",
        "arn:aws:s3:us-east-1:184438910517:accesspoint/bdsp-open-access-point",
    ]
    invalid = [
        "arn:aws:s3:::-noaa-ufs-gefsv13replay-pds",
        "arn:aws:s3::://deafrica-sentinel-5p-co/Sentinel-5p/",
        "arn:aws:s3:::My_Bucket",
        "arn:aws:s3:::bucket-",
        "arn:aws:s3:::ab",
        "arn:aws:s3:::" + "a" * 64,
        "arn:aws:s3:::a..b",
        "arn:aws:s3:::192.168.1.1",
        "arn:aws:s3:::xn--bucket",
        "arn:aws:s3:::my-bucket-s3alias",
    ]

    def check(self, value):
        with contextlib.redirect_stdout(io.StringIO()):
            return ext.ext_resources_arn(value, None, None)

    def test_valid(self):
        for value in self.valid:
            with self.subTest(value=value):
                self.assertTrue(self.check(value))

    def test_invalid(self):
        for value in self.invalid:
            with self.subTest(value=value):
                self.assertFalse(self.check(value))


if __name__ == "__main__":
    unittest.main()
