

# DocumentAccessControlEntry
<a name="API_agent_DocumentAccessControlEntry"></a>

An access control entry specifying a principal and their access level.

## Contents
<a name="API_agent_DocumentAccessControlEntry_Contents"></a>

 ** access **   <a name="bedrock-Type-agent_DocumentAccessControlEntry-access"></a>
Whether to allow or deny access.  
Type: String  
Valid Values: `ALLOW | DENY`   
Required: Yes

 ** name **   <a name="bedrock-Type-agent_DocumentAccessControlEntry-name"></a>
The user identifier.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** type **   <a name="bedrock-Type-agent_DocumentAccessControlEntry-type"></a>
The type of principal.  
Type: String  
Valid Values: `USER`   
Required: Yes

## See Also
<a name="API_agent_DocumentAccessControlEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DocumentAccessControlEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DocumentAccessControlEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DocumentAccessControlEntry) 