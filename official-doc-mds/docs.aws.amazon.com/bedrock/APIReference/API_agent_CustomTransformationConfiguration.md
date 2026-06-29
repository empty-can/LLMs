

# CustomTransformationConfiguration
<a name="API_agent_CustomTransformationConfiguration"></a>

Settings for customizing steps in the data source content ingestion pipeline.

You can configure the data source to process documents with a Lambda function after they are parsed and converted into chunks. When you add a post-chunking transformation, the service stores chunked documents in an S3 bucket and invokes a Lambda function to process them.

To process chunked documents with a Lambda function, define an S3 bucket path for input and output objects, and a transformation that specifies the Lambda function to invoke. You can use the Lambda function to customize how chunks are split, and the metadata for each chunk. 

## Contents
<a name="API_agent_CustomTransformationConfiguration_Contents"></a>

 ** intermediateStorage **   <a name="bedrock-Type-agent_CustomTransformationConfiguration-intermediateStorage"></a>
An S3 bucket path for input and output objects.  
Type: [IntermediateStorage](API_agent_IntermediateStorage.md) object  
Required: Yes

 ** transformations **   <a name="bedrock-Type-agent_CustomTransformationConfiguration-transformations"></a>
A Lambda function that processes documents.  
Type: Array of [Transformation](API_agent_Transformation.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

## See Also
<a name="API_agent_CustomTransformationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CustomTransformationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CustomTransformationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CustomTransformationConfiguration) 