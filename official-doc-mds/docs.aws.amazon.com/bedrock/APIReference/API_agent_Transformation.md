

# Transformation
<a name="API_agent_Transformation"></a>

A custom processing step for documents moving through a data source ingestion pipeline. To process documents after they have been converted into chunks, set the step to apply to `POST_CHUNKING`.

## Contents
<a name="API_agent_Transformation_Contents"></a>

 ** stepToApply **   <a name="bedrock-Type-agent_Transformation-stepToApply"></a>
When the service applies the transformation.  
Type: String  
Valid Values: `POST_CHUNKING`   
Required: Yes

 ** transformationFunction **   <a name="bedrock-Type-agent_Transformation-transformationFunction"></a>
A Lambda function that processes documents.  
Type: [TransformationFunction](API_agent_TransformationFunction.md) object  
Required: Yes

## See Also
<a name="API_agent_Transformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/Transformation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/Transformation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/Transformation) 