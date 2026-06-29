

# OnlineEvaluationConfigSource
<a name="API_OnlineEvaluationConfigSource"></a>

A reference to an existing online evaluation configuration to use as the data source for batch evaluation.

## Contents
<a name="API_OnlineEvaluationConfigSource_Contents"></a>

 ** onlineEvaluationConfigArn **   <a name="BedrockAgentCore-Type-OnlineEvaluationConfigSource-onlineEvaluationConfigArn"></a>
The Amazon Resource Name (ARN) of the online evaluation configuration to use as the session source.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** timeRange **   <a name="BedrockAgentCore-Type-OnlineEvaluationConfigSource-timeRange"></a>
Optional session filter configuration to narrow down which sessions from the online evaluation configuration to include.  
Type: [SessionFilterConfig](API_SessionFilterConfig.md) object  
Required: No

## See Also
<a name="API_OnlineEvaluationConfigSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/OnlineEvaluationConfigSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/OnlineEvaluationConfigSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/OnlineEvaluationConfigSource) 