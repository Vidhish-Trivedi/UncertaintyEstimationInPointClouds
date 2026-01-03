import pdal
import json

pipeline_json = {
    "pipeline": [
        "C:\\Users\\Vidhish17\\Desktop\\final\\Urban_PointCloud_Processing\\datasets\\ahn\\ahn_2386_9702.laz",
        {
            "type": "filters.smrf",
            "window": 18.0,
            "threshold": 0.5,
            "slope": 0.15,
            "cell": 1.0,
            "scalar": 1.25,
            "cut": 0.0,
            "returns": "last"
        },
        {
            "type": "writers.las",
            "filename": "ground_classified.laz"
        }
    ]
}

pipeline = pdal.Pipeline(json.dumps(pipeline_json))
pipeline.execute()
print("Ground classification done!")
