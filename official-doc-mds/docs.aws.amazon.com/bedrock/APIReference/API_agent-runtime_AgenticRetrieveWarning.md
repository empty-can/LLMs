

# AgenticRetrieveWarning
<a name="API_agent-runtime_AgenticRetrieveWarning"></a>

A warning generated during agentic retrieval.

## Contents
<a name="API_agent-runtime_AgenticRetrieveWarning_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** guardrail **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveWarning-guardrail"></a>
A warning from a guardrail evaluation.  
Type: [AgenticRetrieveGuardrailWarning](API_agent-runtime_AgenticRetrieveGuardrailWarning.md) object  
Required: No

 ** message **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveWarning-message"></a>
A general warning message.  
Type: [AgenticRetrieveWarningMessage](API_agent-runtime_AgenticRetrieveWarningMessage.md) object  
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveWarning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveWarning) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveWarning) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveWarning) 