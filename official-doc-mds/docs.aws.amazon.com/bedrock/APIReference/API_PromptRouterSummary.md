

# PromptRouterSummary
<a name="API_PromptRouterSummary"></a>

Details about a prompt router.

## Contents
<a name="API_PromptRouterSummary_Contents"></a>

 ** fallbackModel **   <a name="bedrock-Type-PromptRouterSummary-fallbackModel"></a>
The router's fallback model.  
Type: [PromptRouterTargetModel](API_PromptRouterTargetModel.md) object  
Required: Yes

 ** models **   <a name="bedrock-Type-PromptRouterSummary-models"></a>
The router's models.  
Type: Array of [PromptRouterTargetModel](API_PromptRouterTargetModel.md) objects  
Required: Yes

 ** promptRouterArn **   <a name="bedrock-Type-PromptRouterSummary-promptRouterArn"></a>
The router's ARN.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:default-prompt-router/[a-zA-Z0-9-:.]+`   
Required: Yes

 ** promptRouterName **   <a name="bedrock-Type-PromptRouterSummary-promptRouterName"></a>
The router's name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `([0-9a-zA-Z][ _-]?)+`   
Required: Yes

 ** routingCriteria **   <a name="bedrock-Type-PromptRouterSummary-routingCriteria"></a>
The router's routing criteria.  
Type: [RoutingCriteria](API_RoutingCriteria.md) object  
Required: Yes

 ** status **   <a name="bedrock-Type-PromptRouterSummary-status"></a>
The router's status.  
Type: String  
Valid Values: `AVAILABLE`   
Required: Yes

 ** type **   <a name="bedrock-Type-PromptRouterSummary-type"></a>
The summary's type.  
Type: String  
Valid Values: `custom | default`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-PromptRouterSummary-createdAt"></a>
When the router was created.  
Type: Timestamp  
Required: No

 ** description **   <a name="bedrock-Type-PromptRouterSummary-description"></a>
The router's description.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `([0-9a-zA-Z:.][ _-]?)+`   
Required: No

 ** updatedAt **   <a name="bedrock-Type-PromptRouterSummary-updatedAt"></a>
When the router was updated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_PromptRouterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/PromptRouterSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/PromptRouterSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/PromptRouterSummary) 