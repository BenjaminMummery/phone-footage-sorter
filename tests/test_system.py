# Copyright (c) 2023 Benjamin Mummery

import os


class TestSetup:
    @staticmethod
    def test_install(virtualenv, tmp_path):
        virtualenv.run(f"python -m pip install {os.getcwd()}")
        virtualenv.run(f"cd {tmp_path} && phone-footage-sorter")


class TestRun:
    @staticmethod
    def test_flat_folder(virtualenv, tmp_path):
        infiles = ["20220202_222222.mp4", "20220203_222222.mp4", "20220203_222223.mp4"]
        outfiles = [
            "Training Videos - 2022-02-02.mp4",
            "Training Videos - 2022-02-03 - Part1.mp4",
            "Training Videos - 2022-02-03 - Part2.mp4",
        ]
        for file in infiles:
            (tmp_path / file).write_text("")

        virtualenv.run(f"python -m pip install {os.getcwd()}")
        virtualenv.run(f"cd {tmp_path} && phone-footage-sorter")

        assert set(os.listdir(tmp_path)) == set(outfiles)
