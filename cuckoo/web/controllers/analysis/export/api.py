# Copyright (C) 2010-2013 Claudio Guarnieri.
# Copyright (C) 2014-2016 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from django.http import JsonResponse

from bin.utils import api_post, json_error_response
from controllers.analysis.export.export import ExportController
from controllers.analysis.analysis import AnalysisController

class ExportApi:
    @api_post
    def export_estimate_size(request, body):
        task_id = body.get('task_id')
        taken_dirs = body.get("dirs", [])
        taken_files = body.get("files", [])

        if not taken_dirs and not taken_files:
            return JsonResponse({"size": 0, "size_human": "-"}, safe=False)

        if not task_id:
            return json_error_response("invalid task_id")

        size = ExportController.estimate_size(task_id=task_id,
                                              taken_dirs=taken_dirs,
                                              taken_files=taken_files)

        return JsonResponse(size, safe=False)

    @api_post
    def get_files(request, body):
        task_id = body.get('task_id', None)

        if not task_id:
            return json_error_response("invalid task_id")

        report = AnalysisController.get_report(task_id)
        if not report["analysis"].get("info", {}).get("analysis_path"):
            raise Exception("old-style analysis")

        analysis_path = report["analysis"]["info"]["analysis_path"]

        dirs, files = ExportController.get_files(analysis_path)

        return JsonResponse({"dirs": dirs, "files": files}, safe=False)