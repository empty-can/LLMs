

# UserIdentifier
<a name="API_UserIdentifier"></a>

The OAuth2.0 token or user ID that was used to generate the workload access token used for initiating the user authorization flow to retrieve OAuth2.0 tokens.

## Contents
<a name="API_UserIdentifier_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** userId **   <a name="BedrockAgentCore-Type-UserIdentifier-userId"></a>
The ID of the user for whom you have retrieved a workload access token for  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** userToken **   <a name="BedrockAgentCore-Type-UserIdentifier-userToken"></a>
The OAuth2.0 token issued by the user’s identity provider that was used to generate the workload access token  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 131072.  
Pattern: `[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+.[A-Za-z0-9-_=]+`   
Required: No

## See Also
<a name="API_UserIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UserIdentifier) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UserIdentifier) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UserIdentifier) 