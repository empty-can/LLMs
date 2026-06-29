

# DataSourceType
<a name="API_DataSourceType"></a>

 Source of examples to add to the dataset. 

## Contents
<a name="API_DataSourceType_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** inlineExamples **   <a name="bedrockagentcorecontrol-Type-DataSourceType-inlineExamples"></a>
 Inline examples provided directly in the request body.   
Type: [InlineExamplesSource](API_InlineExamplesSource.md) object  
Required: No

 ** s3Source **   <a name="bedrockagentcorecontrol-Type-DataSourceType-s3Source"></a>
 Amazon S3 URI pointing to a JSONL file in the customer's bucket.   
Type: [S3Source](API_S3Source.md) object  
Required: No

## See Also
<a name="API_DataSourceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DataSourceType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DataSourceType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DataSourceType) 