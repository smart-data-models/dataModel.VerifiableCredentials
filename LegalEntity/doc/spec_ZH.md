<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：法律实体  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/LegalEntity/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：法律实体的**EBSI 可验证 ID 架构**  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `credentialSchema[object]`: 包含有关可验证授权所依据的凭证模式（模板）的信息  	- `id[uri]`: 引用存储在（相关）可信模式注册中心（TSR）上的凭证模式（模板），可验证授权正是基于该模式进行的    
- `credentialStatus[object]`: 包含有关如何验证可核实证明状态的信息（通过撤销和认可注册表，RER）。  	- `id[uri]`: 撤销和认可注册表 (RER) 中的参考记录，以便核查可核实证明的有效性    
	- `statusListCredential[uri]`: 引用 StatusList2021Credential 的 URL    
	- `statusListIndex[string]`: 以字符串形式表示的整数。基于零的索引值标识状态的位位置    
	- `statusPurpose[string]`: 状态条目的目的    
- `credentialSubject[object]`: 定义可验证 ID 所描述的主体信息  	- `EORI[string]`: 凭证主体的经济经营者注册和识别 (EORI)（在欧盟委员会第 1352/2013 号实施细则中提及    
	- `LEI[string]`: 证书主体的正式法律实体标识符 (LEI)（委员会第 1247/2012 号实施细则 (EU) 中所述）    
	- `SEED[string]`: 凭证主体的消费税数据交换系统 (SEED)（即理事会条例 (EC) No 389/2012 第 2(12)条规定的消费税编号）    
	- `SIC[string]`: 证书主体的标准行业分类 (SIC) （欧洲议会和理事会第 2009/101/EC 号指令第 3(1)条。）    
	- `VATRegistration[string]`: 证书主体的增值税号    
	- `domainName[string]`: 证书主体域名    
	- `id[uri]`: 定义可验证证明所述主体的 DID    
	- `identifier[array]`: 待补说明    
	- `legalAddress[string]`: 证书主体的正式法定地址    
	- `legalName[string]`: 证书主体的正式法定名称    
	- `legalPersonIdentifier[string]`: 凭证主体的国家/法定标识符（由发送成员国根据用于跨境身份识别的技术规范制作，并尽可能在时间上保持不变）    
- `evidence[array]`: 包含有关签发可核查证明的程序的信息  - `expirationDate[date-time]`: 定义可验证证明过期的日期和时间  - `id[uri]`: 定义可验证证明的唯一标识符  - `issuanceDate[date-time]`: 定义可验证证明生效的日期和时间  - `issued[date-time]`: 定义可验证证明的签发时间  - `issuer[uri]`: 定义可验证证明的签发人  - `proof[object]`: 包含有关证明的信息  	- `created[date-time]`: 定义创建校样的日期和时间    
	- `jws[string]`: 以 JWS 格式定义证明值    
	- `proofPurpose[string]`: 确定证明的目的    
	- `type[string]`: 定义证明类型    
- `type[array]`: 定义可验证凭据类型  - `validFrom[date-time]`: 定义可验证证明生效的日期和时间  - `validUntil[date-time]`: 定义可验证证明过期的日期和时间  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `credentialSubject`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
源自 EBSI json 模式的数据模型 https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas。@context 属性已从定义中删除，因为它在 NGSI-LD 中是强制性的，不需要明确记录。仅提供键值链接数据中的示例  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
LegalEntity:    
  description: Schema of an EBSI Verifiable ID for a legal entity    
  properties:    
    credentialSchema:    
      description: Contains information about the credential schema (template) on which the Verifiable Authorisation is based    
      properties:    
        id:    
          description: References the credential schema (template) stored on the (relevant) Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines credential schema type    
          enum:    
            - FullJsonSchemaValidator2021    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialStatus:    
      description: 'Contains information about how to verify the status of the Verifiable Attestation (via the Revocation and Endorsement Registry, RER)'    
      properties:    
        id:    
          description: References record in the Revocation and Endorsement Registry (RER) to enable verification of a Verifiable Attestation’s validity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListCredential:    
          description: URL referencing the StatusList2021Credential    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListIndex:    
          description: Integer expressed as a string. The zero based index value identifies the bit position of the status    
          type: string    
          x-ngsi:    
            type: Property    
        statusPurpose:    
          description: Purpose of the status entry    
          enum:    
            - revocation    
            - suspension    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the Verifiable Credential status type    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialSubject:    
      description: Defines information about the subject that is described by the Verifiable ID    
      properties:    
        EORI:    
          description: Economic Operator Registration and Identification (EORI) of Credential Subject (referred to in Commission Implementing Regulation (EU) No 1352/2013)    
          type: string    
          x-ngsi:    
            type: Property    
        LEI:    
          description: Official legal entity identifier (LEI) of Credential Subject (referred to in Commission Implementing Regulation (EU) No 1247/2012)    
          type: string    
          x-ngsi:    
            type: Property    
        SEED:    
          description: System for Exchange of Excise Data (SEED) of Credential Subject (i.e. excise number provided in Article 2(12) of Council Regulation (EC) No 389/2012)    
          type: string    
          x-ngsi:    
            type: Property    
        SIC:    
          description: Standard Industrial Classification (SIC) of Credential Subject (Article 3(1) of Directive 2009/101/EC of the European Parliament and of the Council.)    
          type: string    
          x-ngsi:    
            type: Property    
        VATRegistration:    
          description: VAT number  of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        domainName:    
          description: Domain name  of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        identifier:    
          description: Description to be completed    
          items:    
            properties:    
              id:    
                description: Description to be completed    
                format: uri    
                type: string    
                x-ngsi:    
                  type: Property    
              schemeID:    
                description: Description to be completed    
                type: string    
                x-ngsi:    
                  type: Property    
              value:    
                description: Description to be completed    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
          x-ngsi:    
            type: Property    
        legalAddress:    
          description: Official legal address of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        legalName:    
          description: Official legal name of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        legalPersonIdentifier:    
          description: National/Legal Identifier of Credential Subject (constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time)    
          type: string    
          x-ngsi:    
            type: Property    
        taxReference:    
          description: Official tax reference number of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - legalName    
      type: object    
      x-ngsi:    
        type: Property    
    evidence:    
      description: Contains information about the process which resulted in the issuance of the Verifiable Attestation    
      items:    
        properties:    
          documentPresence:    
            items:    
              description: Description to be completed    
              type: string    
              x-ngsi:    
                type: Property    
            type: array    
          evidenceDocument:    
            items:    
              description: Description to be completed    
              type: string    
              x-ngsi:    
                type: Property    
            type: array    
          id:    
            description: 'If present, it MUST contain a URL that points to where more information about this instance of evidence can be found'    
            type: string    
            x-ngsi:    
              type: Property    
          subjectPresence:    
            description: Description to be completed    
            type: string    
            x-ngsi:    
              type: Property    
          type:    
            description: Defines the evidence type    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        required:    
          - id    
          - type    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    expirationDate:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: Defines unique identifier of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    issuanceDate:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issued:    
      description: Defines when the Verifiable Attestation was issued    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issuer:    
      description: Defines the issuer of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    proof:    
      description: Contains information about the proof    
      properties:    
        created:    
          description: 'Defines the date and time, when the proof has been created'    
          format: date-time    
          type: string    
          x-ngsi:    
            type: Property    
        jws:    
          description: Defines the proof value in JWS format    
          type: string    
          x-ngsi:    
            type: Property    
        proofPurpose:    
          description: Defines the purpose of the proof    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the proof type    
          type: string    
          x-ngsi:    
            type: Property    
        verificationMethod:    
          description: Contains information about the verification method / proof mechanisms    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - type    
        - proofPurpose    
        - created    
        - verificationMethod    
        - jws    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: Defines the Verifiable Credential type    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validUntil:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - credentialSubject    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-vid/legal-entity/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/LegalEntity/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
以 JSON-LD 格式作为键值的 LegalEntity 示例不可用。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
未提供规范化的 JSON-LD 格式 LegalEntity 示例。在不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
#### LegalEntity NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 LegalEntity 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "https://www.w3.org/2018/credentials/v1",  
    "https://europa.eu/schemas/v-id/2020/v1",  
    "https://europa.eu/schemas/eidas/2020/v1"  
  ],  
  "id": "urn:did:123456",  
  "type": ["VerifiableCredential", "VerifiableAttestation"],  
  "issuer": "did:ebsi:2757945549477fc571663bee12042873fe555b674bd294a3",  
  "issuanceDate": "2019-06-22T14:11:44Z",  
  "validFrom": "2019-06-22T14:11:44Z",  
  "issued": "2019-06-22T14:11:44Z",  
  "credentialSubject": {  
    "id": "did:ebsi:2659b154a445434a39d91149ead3bd993cb99fd5e78281b7",  
    "identifier": [  
      {  
        "schemeID": "SHACL",  
        "value": "SHACL ID 1",  
        "id": "http://student.id/41231232"  
      }  
    ],  
    "legalName": "Example Company"  
  },  
  "credentialStatus": {  
    "id": "https://europa.eu/status/identity#1dee355d-0432-4910-ac9c-70d89e8d674e",  
    "type": "CredentialStatusList2020"  
  },  
  "credentialSchema": {  
    "id": "https://europa.eu/tsr-vid/verifiableid1.json",  
    "type": "FullJsonSchemaValidator2021"  
  },  
  "evidence": [  
    {  
      "id": "https://europa.eu/tsr-vid/evidence/f2aeec97-fc0d-42bf-8ca7-0548192d4231",  
      "type": ["DocumentVerification"],  
      "verifier": "did:ebsi:2e81454f76775c687694ee6772a17796436768a30e289555",  
      "evidenceDocument": ["Passport"],  
      "subjectPresence": "Physical",  
      "documentPresence": ["Physical"]  
    }  
  ],  
  "proof": {  
    "type": "EidasSeal2021",  
    "created": "2019-06-22T14:11:44Z",  
    "proofPurpose": "assertionMethod",  
    "verificationMethod": "did:ebsi:2757945549477fc571663bee12042873fe555b674bd294a3#2368332668",  
    "jws": "HG21J4fdlnBvBA+y6D...amP7O="  
  }  
}  
```  
</details>  
不提供规范化的 JSON-LD 格式 LegalEntity 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
