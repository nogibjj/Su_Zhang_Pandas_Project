from main import describe_stat, group_by, build_histogram


def test_describe_stat():
    """testing out if describe_stat function works"""
    output = describe_stat()
    assert output is not None


def test_group_by():
    """testing out if group_by function works"""
    output_grouby = group_by("Blood Type")
    assert output_grouby is not None


def test_build_histogram():
    """testing out if build_histogram works"""
    output_hist = build_histogram()
    assert output_hist is None


if __name__ == "__main__":
    test_describe_stat()
    test_group_by()
    test_build_histogram()
