

# BrowserSummary
<a name="API_BrowserSummary"></a>

Contains summary information about a browser. A browser enables Amazon Bedrock AgentCore Agent to interact with web content.

## Contents
<a name="API_BrowserSummary_Contents"></a>

 ** browserArn **   <a name="bedrockagentcorecontrol-Type-BrowserSummary-browserArn"></a>
The Amazon Resource Name (ARN) of the browser.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):browser(-custom)?/(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: Yes

 ** browserId **   <a name="bedrockagentcorecontrol-Type-BrowserSummary-browserId"></a>
The unique identifier of the browser.  
Type: String  
Pattern: `(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-BrowserSummary-createdAt"></a>
The timestamp when the browser was created.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-BrowserSummary-status"></a>
The current status of the browser.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | READY | DELETING | DELETE_FAILED | DELETED`   
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-BrowserSummary-description"></a>
The description of the browser.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** lastUpdatedAt **   <a name="bedrockagentcorecontrol-Type-BrowserSummary-lastUpdatedAt"></a>
The timestamp when the browser was last updated.  
Type: Timestamp  
Required: No

 ** name **   <a name="bedrockagentcorecontrol-Type-BrowserSummary-name"></a>
The name of the browser.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: No

## See Also
<a name="API_BrowserSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/BrowserSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/BrowserSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/BrowserSummary) 