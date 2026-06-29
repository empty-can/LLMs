

# IamPrincipal
<a name="API_IamPrincipal"></a>

An IAM principal specification for rule matching.

## Contents
<a name="API_IamPrincipal_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-IamPrincipal-arn"></a>
The Amazon Resource Name (ARN) of the IAM principal. Supports user, role, and assumed-role ARNs. Wildcards can be used with the `StringLike` operator.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws[a-zA-Z-]*:iam::(\d{12}|\*):(user|role)/[\w+=,.@*?/-]+|arn:aws[a-zA-Z-]*:sts::(\d{12}|\*):assumed-role/[\w+=,.@*?/-]+)`   
Required: Yes

 ** operator **   <a name="bedrockagentcorecontrol-Type-IamPrincipal-operator"></a>
The match operator. `StringEquals` requires an exact match. `StringLike` supports wildcard patterns using `*` and `?`.  
Type: String  
Valid Values: `StringEquals | StringLike`   
Required: No

## See Also
<a name="API_IamPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/IamPrincipal) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/IamPrincipal) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/IamPrincipal) 