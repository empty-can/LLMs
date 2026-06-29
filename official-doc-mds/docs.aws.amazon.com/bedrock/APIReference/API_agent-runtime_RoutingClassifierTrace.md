

# RoutingClassifierTrace
<a name="API_agent-runtime_RoutingClassifierTrace"></a>

A trace for a routing classifier.

## Contents
<a name="API_agent-runtime_RoutingClassifierTrace_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** invocationInput **   <a name="bedrock-Type-agent-runtime_RoutingClassifierTrace-invocationInput"></a>
The classifier's invocation input.  
Type: [InvocationInput](API_agent-runtime_InvocationInput.md) object  
Required: No

 ** modelInvocationInput **   <a name="bedrock-Type-agent-runtime_RoutingClassifierTrace-modelInvocationInput"></a>
The classifier's model invocation input.  
Type: [ModelInvocationInput](API_agent-runtime_ModelInvocationInput.md) object  
Required: No

 ** modelInvocationOutput **   <a name="bedrock-Type-agent-runtime_RoutingClassifierTrace-modelInvocationOutput"></a>
The classifier's model invocation output.  
Type: [RoutingClassifierModelInvocationOutput](API_agent-runtime_RoutingClassifierModelInvocationOutput.md) object  
Required: No

 ** observation **   <a name="bedrock-Type-agent-runtime_RoutingClassifierTrace-observation"></a>
The classifier's observation.  
Type: [Observation](API_agent-runtime_Observation.md) object  
Required: No

## See Also
<a name="API_agent-runtime_RoutingClassifierTrace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RoutingClassifierTrace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RoutingClassifierTrace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RoutingClassifierTrace) 