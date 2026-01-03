import pdal, json

pipeline_json = {
    "pipeline": [
        "with_hag.laz",
        {
            "type": "filters.assign",
            "value": [
                # Ground
                "Classification = 2 WHERE HeightAboveGround < 0.15",

                # Low vegetation → height above ground ≥0.15
                "Classification = 3 WHERE HeightAboveGround >= 0.15",

                # Medium vegetation → height above ground ≥0.5
                "Classification = 4 WHERE HeightAboveGround >= 0.5",

                # High vegetation → height above ground ≥2.0
                "Classification = 5 WHERE HeightAboveGround >= 2.0",

                # Buildings → height above ground ≥3.0
                "Classification = 6 WHERE HeightAboveGround >= 3.0"
            ]
        },
        {
            "type": "writers.las",
            "filename": "final_refined_classified.laz"
        }
    ]
}

p = pdal.Pipeline(json.dumps(pipeline_json))
p.execute()
print("Classification done!")
