# -*- coding: utf-8 -*-

# Copyright (c) 2018 Minoru Osuka
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib


def get_instance(class_name, **class_args):
    class_data = class_name.split('.')

    module_path = '.'.join(class_data[:-1])
    class_name = class_data[-1]

    module = importlib.import_module(module_path)
    class_obj = getattr(module, class_name)

    if class_args:
        return class_obj(**class_args)
    else:
        return class_obj()
