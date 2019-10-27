import unittest

import gila


class TestGila(unittest.TestCase):

    def setUp(self):
        gila.reset()

    def test_reset(self):
        key = "key"
        value = "value"
        gila.set(key, value)
        gila.reset()
        self.assertIsNone(gila.get(key))

    def test_setting_values(self):
        key = "key"
        value = "value"
        gila.set(key, value)
        self.assertEqual(gila.get(key), value)

    def test_setting_default(self):
        key = "key"
        value = "value"
        gila.set_default(key, value)
        self.assertEqual(gila.get(key), value)

    def test_override_precedence_default(self):
        key = "key"
        default_value = "test"
        override_value = "value"
        gila.set_default(key, default_value)
        self.assertEqual(gila.get(key), default_value)
        gila.set(key, override_value)
        self.assertEqual(gila.get(key), override_value)
        

    def test_read_in_yaml(self):
        gila.set_config_name('yaml_config')
        gila.add_config_path('./tests/configs')
        gila.read_in_config()
        self.assertEqual(True, gila.get("exists"))
        self.assertEqual('yaml_config', gila.get("meta.filename"))
        self.assertIsInstance(gila.get("contents"), list)

    def test_read_in_prop(self):
        gila.set_config_name('prop_config')
        gila.add_config_path('./tests/configs')
        gila.read_in_config()
        self.assertEqual('True', gila.get("exists"))
        self.assertEqual('string', gila.get("contents.filetype.value_type"))
        self.assertIsNone(gila.get("contents"))


if __name__ == '__main__':
    unittest.main()
