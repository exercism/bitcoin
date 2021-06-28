import hashlib
import unittest

from get_block_header import get_block_header


class BlockHeaderTest(unittest.TestCase):

    def test_block_header(self):
        """Check the hash of the block header 500000
        """

        # Get block header 500000
        block_header = get_block_header(500000)

        # Check that the format of block_header is (hex) str
        # Hint: check the options for the RPC calls you're making (e.g. verbose mode)
        self.assertIsInstance(block_header, str)

        # Check the SHA1 hash of the block header against hardcoded value
        self.assertEqual(hashlib.sha1(bytes.fromhex(block_header)).hexdigest(), "04be9aee3927cc2a40b8d1116e68e3d50e13fc58")


if __name__ == "__main__":
    unittest.main()
