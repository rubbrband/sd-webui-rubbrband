import modules.scripts as scripts
import gradio as gr
from modules.processing import Processed
import requests
import uuid

class Script(scripts.Script):
    def title(self):
        return "Rubbrband Image Hosting Service"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        api_key = gr.Textbox(value="", label="Rubbrband API Key")
        return [api_key]
    def postprocess(self, p, processed: Processed, rubbrband_api_key):
        for image in processed.images:
            image_id = str(uuid.uuid4())
            image_json_data = {
                "api_key": rubbrband_api_key,
                "prompt": p.prompt,
                "negative_prompt": p.negative_prompt,
                "seed": p.seed,
                "n_iter": p.n_iter,
                "steps": p.steps,
                "cfg_scale": p.cfg_scale,
                "width": p.width,
                "height": p.height,
                "sampler_name": p.sampler_name,
                "sd_model_name": p.sd_model_name,
                "image": image,
                "is_img2img": self.is_img2img,
                "image_id": image_id,
            }
            if self.is_img2img:
                image_json_data["init_images"] = p.init_images
            requests.post(
                "https://block.rubbrband.com/upload_barth_img",
                json=image_json_data,
            )
        return p