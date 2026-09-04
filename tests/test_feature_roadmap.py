from advanced_features.feature_roadmap import FeatureRoadmap


def test_feature_roadmap():
    roadmap = FeatureRoadmap()

    result = roadmap.generate()

    assert "roadmap" in result
    assert len(result["roadmap"]) == 3
    assert result["status"] == "proposed"