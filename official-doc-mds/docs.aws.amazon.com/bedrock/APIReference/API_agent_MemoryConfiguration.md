

# MemoryConfiguration
<a name="API_agent_MemoryConfiguration"></a>

Details of the memory configuration.

## Contents
<a name="API_agent_MemoryConfiguration_Contents"></a>

 ** enabledMemoryTypes **   <a name="bedrock-Type-agent_MemoryConfiguration-enabledMemoryTypes"></a>
The type of memory that is stored.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Valid Values: `SESSION_SUMMARY`   
Required: Yes

 ** sessionSummaryConfiguration **   <a name="bedrock-Type-agent_MemoryConfiguration-sessionSummaryConfiguration"></a>
Contains the configuration for SESSION\_SUMMARY memory type enabled for the agent.   
Type: [SessionSummaryConfiguration](API_agent_SessionSummaryConfiguration.md) object  
Required: No

 ** storageDays **   <a name="bedrock-Type-agent_MemoryConfiguration-storageDays"></a>
The number of days the agent is configured to retain the conversational context.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 365.  
Required: No

## See Also
<a name="API_agent_MemoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/MemoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/MemoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/MemoryConfiguration) 