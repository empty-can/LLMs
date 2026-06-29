

# CodeInterpreterSummary
<a name="API_CodeInterpreterSummary"></a>

Contains summary information about a code interpreter. A code interpreter enables Amazon Bedrock AgentCore Agent to execute code.

## Contents
<a name="API_CodeInterpreterSummary_Contents"></a>

 ** codeInterpreterArn **   <a name="bedrockagentcorecontrol-Type-CodeInterpreterSummary-codeInterpreterArn"></a>
The Amazon Resource Name (ARN) of the code interpreter.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):code-interpreter(-custom)?/(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: Yes

 ** codeInterpreterId **   <a name="bedrockagentcorecontrol-Type-CodeInterpreterSummary-codeInterpreterId"></a>
The unique identifier of the code interpreter.  
Type: String  
Pattern: `(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-CodeInterpreterSummary-createdAt"></a>
The timestamp when the code interpreter was created.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-CodeInterpreterSummary-status"></a>
The current status of the code interpreter.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | READY | DELETING | DELETE_FAILED | DELETED`   
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-CodeInterpreterSummary-description"></a>
The description of the code interpreter.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** lastUpdatedAt **   <a name="bedrockagentcorecontrol-Type-CodeInterpreterSummary-lastUpdatedAt"></a>
The timestamp when the code interpreter was last updated.  
Type: Timestamp  
Required: No

 ** name **   <a name="bedrockagentcorecontrol-Type-CodeInterpreterSummary-name"></a>
The name of the code interpreter.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: No

## See Also
<a name="API_CodeInterpreterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CodeInterpreterSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CodeInterpreterSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CodeInterpreterSummary) 