from pipeline.pipeline_runner.pipeline_processor_run import run_pipeline

if __name__=="__main__":
    input_file=input("Enter Excel file path: ").strip()

    run_pipeline(input_file=input_file,
                 max_workers=None,
                 )
