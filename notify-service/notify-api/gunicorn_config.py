# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The configuration for gunicorn, which picks up the
runtime options from environment variables.

The best practice so far is For environments with multiple CPU cores, increase the number of workers to be equal to
the cores available. Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance
scaling. Adjust the number of workers and threads on a per-application basis.
"""

import os

workers = int(os.environ.get("GUNICORN_PROCESSES", "1"))  # pylint: disable=invalid-name
threads = int(os.environ.get("GUNICORN_THREADS", "8"))  # pylint: disable=invalid-name
timeout = int(os.environ.get("GUNICORN_TIMEOUT", "0"))  # pylint: disable=invalid-name

forwarded_allow_ips = "*"  # pylint: disable=invalid-name
secure_scheme_headers = {"X-Forwarded-Proto": "https"}  # pylint: disable=invalid-name
