"""
This module is used to update the copier context.
"""


from copier_templates_extensions import ContextHook

class ContextUpdater(ContextHook):
    update = False

    def hook(self, context):
        # Split (namespace/)repository:tag into (namespace/)repository and tag
        base_image = context["base_image"]
        context["repository"] = base_image.split(":")[0]
        context["tag"] = base_image.split(":")[-1]

        context["pod_tag"] = context["tag"] + "_distributed"
        context["pod_image"] = context["repository"] + ":" + context["pod_tag"]