import pdal
import json

pipeline_json = {
    "pipeline": [
        "ground_classified.laz",
        {
            "type": "filters.hag_nn"
        },
        {
            "type": "writers.las",
            "filename": "with_hag.laz",
            "extra_dims": "HeightAboveGround=float32"
        }
    ]
}

pipeline = pdal.Pipeline(json.dumps(pipeline_json))
pipeline.execute()
print("HeightAboveGround added!")
