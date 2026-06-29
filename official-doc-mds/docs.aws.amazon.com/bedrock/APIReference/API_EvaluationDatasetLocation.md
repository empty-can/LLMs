

# EvaluationDatasetLocation
<a name="API_EvaluationDatasetLocation"></a>

The location in Amazon S3 where your prompt dataset is stored.

## Contents
<a name="API_EvaluationDatasetLocation_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3Uri **   <a name="bedrock-Type-EvaluationDatasetLocation-s3Uri"></a>
The S3 URI of the S3 bucket specified in the job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][-.a-z0-9]{1,61}[a-z0-9](?:/[-!_*'().a-z0-9A-Z]+(?:/[-!_*'().a-z0-9A-Z]+)*)?/?`   
Required: No

## See Also
<a name="API_EvaluationDatasetLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationDatasetLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationDatasetLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationDatasetLocation) 