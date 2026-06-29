

# CachePointBlock
<a name="API_runtime_CachePointBlock"></a>

Defines a section of content to be cached for reuse in subsequent API calls.

## Contents
<a name="API_runtime_CachePointBlock_Contents"></a>

 ** type **   <a name="bedrock-Type-runtime_CachePointBlock-type"></a>
Specifies the type of cache point within the CachePointBlock.  
Type: String  
Valid Values: `default`   
Required: Yes

 ** ttl **   <a name="bedrock-Type-runtime_CachePointBlock-ttl"></a>
Optional TTL duration for cache entries. When specified, enables extended TTL caching with the specified duration. When omitted, uses `type` value for caching behavior.  
Type: String  
Valid Values: `5m | 1h`   
Required: No

## See Also
<a name="API_runtime_CachePointBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/CachePointBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/CachePointBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/CachePointBlock) 