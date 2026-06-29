

# CacheDetail
<a name="API_runtime_CacheDetail"></a>

Cache creation metrics for a specific TTL duration

## Contents
<a name="API_runtime_CacheDetail_Contents"></a>

 ** inputTokens **   <a name="bedrock-Type-runtime_CacheDetail-inputTokens"></a>
Number of tokens written to cache with this TTL (cache creation tokens)  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: Yes

 ** ttl **   <a name="bedrock-Type-runtime_CacheDetail-ttl"></a>
TTL duration for these cached tokens  
Type: String  
Valid Values: `5m | 1h`   
Required: Yes

## See Also
<a name="API_runtime_CacheDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/CacheDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/CacheDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/CacheDetail) 