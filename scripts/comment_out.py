import os
import sys
import re

from modules import scripts

class CommentOutScript(scripts.Script):
    def title(self):
        return "Prompt Comment Out"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def replace_comment(self, text):
        return re.sub('/=.*?=/', '', text)

    def replace_all_prompt(self, all_prompts):
        for i in range(len(all_prompts)):
            prompt = all_prompts[i]
            prompt = self.replace_comment(prompt)
            all_prompts[i] = prompt

    def process(self, p):
        original_prompt = p.all_prompts[0]
        original_negative_prompt = p.all_negative_prompts[0]
        self.replace_all_prompt(p.all_prompts)
        self.replace_all_prompt(p.all_negative_prompts)
        if original_prompt != p.all_prompts[0]:
            p.extra_generation_params["Positvie with Comment"] = original_prompt
        if original_negative_prompt != p.all_negative_prompts[0]:
            p.extra_generation_params["Negative with Comment"] = original_negative_prompt
