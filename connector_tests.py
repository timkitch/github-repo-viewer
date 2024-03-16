import unittest
from unittest.mock import patch
from GitHubApiConnector import GitHubApiConnector

class TestGitHubApiConnector(unittest.TestCase):
    def setUp(self):
        self.connector = GitHubApiConnector('test_token')

    @patch('requests.get')
    def test_fetch_file_content_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'test content'
        mock_get.return_value.encoding = 'utf-8'

        content, encoding = self.connector.fetch_file_content('http://testurl.com')

        self.assertEqual(content, b'test content')
        self.assertEqual(encoding, 'utf-8')
        mock_get.assert_called_once_with('http://testurl.com', headers={"Authorization": "Bearer test_token"})

    @patch('requests.get')
    def test_fetch_file_content_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        with self.assertRaises(Exception) as context:
            self.connector.fetch_file_content('http://testurl.com')

        self.assertTrue('Failed to fetch file content: 404' in str(context.exception))
        mock_get.assert_called_once_with('http://testurl.com', headers={"Authorization": "Bearer test_token"})

if __name__ == '__main__':
    unittest.main()