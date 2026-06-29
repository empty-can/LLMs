

# BrowserProfileSummary
<a name="API_BrowserProfileSummary"></a>

Contains summary information about a browser profile. A browser profile stores persistent browser data that can be reused across browser sessions.

## Contents
<a name="API_BrowserProfileSummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-createdAt"></a>
The timestamp when the browser profile was created.  
Type: Timestamp  
Required: Yes

 ** lastUpdatedAt **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-lastUpdatedAt"></a>
The timestamp when the browser profile was last updated.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-name"></a>
The name of the browser profile.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** profileArn **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-profileArn"></a>
The Amazon Resource Name (ARN) of the browser profile.  
Type: String  
Pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:browser-profile/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** profileId **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-profileId"></a>
The unique identifier of the browser profile.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-status"></a>
The current status of the browser profile. Possible values include READY, SAVING, DELETING, and DELETED.  
Type: String  
Valid Values: `READY | DELETING | DELETED | SAVING`   
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-description"></a>
The description of the browser profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** lastSavedAt **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-lastSavedAt"></a>
The timestamp when browser session data was last saved to this profile.  
Type: Timestamp  
Required: No

 ** lastSavedBrowserId **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-lastSavedBrowserId"></a>
The identifier of the browser from which data was last saved to this profile.  
Type: String  
Pattern: `(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: No

 ** lastSavedBrowserSessionId **   <a name="bedrockagentcorecontrol-Type-BrowserProfileSummary-lastSavedBrowserSessionId"></a>
The identifier of the browser session from which data was last saved to this profile.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: No

## See Also
<a name="API_BrowserProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/BrowserProfileSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/BrowserProfileSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/BrowserProfileSummary) 