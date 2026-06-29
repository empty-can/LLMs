

# RecommendationSummary
<a name="API_RecommendationSummary"></a>

Summary information about a recommendation.

## Contents
<a name="API_RecommendationSummary_Contents"></a>

 ** createdAt **   <a name="BedrockAgentCore-Type-RecommendationSummary-createdAt"></a>
The timestamp when the recommendation was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-RecommendationSummary-name"></a>
The name of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`   
Required: Yes

 ** recommendationArn **   <a name="BedrockAgentCore-Type-RecommendationSummary-recommendationArn"></a>
The Amazon Resource Name (ARN) of the recommendation.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:recommendation/[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}`   
Required: Yes

 ** recommendationId **   <a name="BedrockAgentCore-Type-RecommendationSummary-recommendationId"></a>
The unique identifier of the recommendation.  
Type: String  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-RecommendationSummary-status"></a>
The current status of the recommendation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | DELETING`   
Required: Yes

 ** type **   <a name="BedrockAgentCore-Type-RecommendationSummary-type"></a>
The type of recommendation.  
Type: String  
Valid Values: `SYSTEM_PROMPT_RECOMMENDATION | TOOL_DESCRIPTION_RECOMMENDATION`   
Required: Yes

 ** updatedAt **   <a name="BedrockAgentCore-Type-RecommendationSummary-updatedAt"></a>
The timestamp when the recommendation was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-RecommendationSummary-description"></a>
The description of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.  
Required: No

## See Also
<a name="API_RecommendationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecommendationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecommendationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecommendationSummary) 