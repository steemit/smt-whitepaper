## 문서 메타데이터
---
- 제작자: @ned; @theoretical
- 개발자: @theoretical; @vandeberg; @itwasntme; @zgredek; @pychol-mychol; @small.minion; @youkaicountry; @picokernel
- 기여자: @sneak; @vandeberg; @valzav; @youkaicountry; @justinw; @goldibex; 그 외
- 스케치 디자이너: @pkattera
- 저작권: Steemit, Inc. 2017
- 깃허브: https://github.com/steemit/smt-whitepaper/blob/master/smt-manual/manual.md
- 번역: @yguhan; 지원: @clayop

## 스마트 미디어 토큰(SMTs)
---
### 콘텐츠 웹사이트, 애플리케이션, 온라인 커뮤니티, 자금 조달을 원하는 협회, 수익 창출과 사용자 수 증가를 위한 토큰 프로토콜
---
[스팀](https://steem.io/steem-bluepaper.pdf)의 스마트 미디어 토큰은 누구나 출시하고 판매할 수 있는 [창작 증명(Proof-of-Brain) [1]](https://steem.io/steem-bluepaper.pdf) 토큰입니다. 스마트 미디어 토큰은 업보트와 “좋아요” 기반의 알고리즘에 의해 분배 되며, 웹사이트와  통합하여 경제적 유인, 성장 촉진을 추구하는 지속 가능한 화폐 중심의 소득 모델입니다. 이 모델은 테스트 단계로  [steemit.com](https://steemit.com), [busy.org](https://busy.org/), [chainbb.com](https://chainbb.com/), [dsound.audio](https://dsound.audio/), [dtube.video](https://dtube.video/)와 다른 스팀 인터페이스들을 통해 새로운 방식으로 콘텐츠, 토큰, 미디어를 창출하며 가치를 증명하고 있습니다.

임의의 토큰 생성과 출시를 허용하는 토큰 프로토콜로 유명한 이더리움 ERC-20 등이 있지만, 사용자와 애플리케이션간의 인센티브 조정을 통해 콘텐츠 비즈니스에서의 토큰 사용성을 극대화하는 프로토콜은 존재하지 않았습니다. 보팅이나 포스팅같은 기본적인 동작에서도 수수료가 발생하는 차선의 트랙잭션 비용 모델 구조로 인해 창작 증명(Proof-of-Brain)에 기반하여 설계되지 않은 메타 토큰과 코어 토큰사이의 이해관계 불일치, 사회 금융적 운영을 수용하지 않는 개인키 계층 구조, 실시간 웹사이트와 동기화되지 않는 느린 트랜잭션 속도 같은 문제가 발생했습니다. 지금까지 어떤 프로토콜도 트위터, 레딧(혹은 서브레딧), 뉴욕 타임즈와 같은 콘텐츠 웹사이트에 적합한 유저 인터페이스를 제공하지 못했습니다.

콘텐츠 웹사이트 및 토큰의 경우 웹사이트와 사용자간의 인센티브 조정은 안정적일뿐만 아니라 분산되고 수학적으로 보장되야 합니다. 새로운 토큰 출시와 인센티브는 블로거, 비디오 블로거, 댓글 작성자와 큐레이터를 포함한 사용자에게 할당되어야 합니다. 새로운 토큰은 게임을 방지하고 상대방의 필요성을 제거하기 위해 지분 가중치된 보팅에 기반하여 배분됩니다. 우수한 사용자 경험은 안전하게 거래되는 토큰(동작별로 구분되는 개인키를 갖습니다)과, 무수수료, 실시간 속도로부터 비롯됩니다. ICO에서 자본을 조달할 수 있는 회사 역량에 따라 인센티브는 조정됩니다. 모든 스마트 미디어 토큰은 ICO 지원 기능이 내장되어 있어, 발행자가 원하면 발급 가능합니다.
## 도입
---
스마트 미디어 토큰은 스팀 블록체인에서의 합의 수준 토큰 발행 프로토콜을 만들기 위한 제안입니다. 콘텐츠 제작자들에 대한 자동 보상 배분 기능을 포함한 스팀 토큰의 혁신적인 특성에서 영감을 받아, 스마트 미디어 토큰은 웹사이트 통합과 애플리케이션 층에서의 신중하게 설계된 프로그래밍화된 토큰 판매, 자동화된 유동성 공급자, 분산화 토큰 시장, 동적 토큰 변수, 대규모 도구(오픈 소스 지갑, 공유 키 서명 도구 등) 생태계 덕분에 이전에 생성되었던 블록체인 토큰 발생 프로토콜을 넘어선 개선판이 될 것입니다.

스마트 미디어 토큰은 스팀과 [steemit.com](https://steemit.com)을 비롯한 스팀 기반 소셜 웹 서비스(steemit.com은 최신 1년 기준 알렉사 랭킹에서 2100권으로 성장한, 스팀의 보상 모델을 통합한 웹사이트입니다)와의 성공적인 관계를 진화 시킬 것입니다. 스마트 미디어 토큰을 통해 웹사이트나 인터넷 콘텐츠 라이브러리는 하나 또는 그 이상의 토큰을 그들의 인터페이스에 통합함으로써 투자금 모금과 자율적 성장을 촉진할 수 있을 것입니다.

스마트 미디어 토큰은 초기에 창의적으로 구조화하거나 시간에 따라 조정될 수 있는 다양한 변수를 커뮤니티에 알맞은 값으로 선택하여 통합함으로써 유연하게 동작할 수 있도록 설계되었습니다. 스마트 미디어 토큰의 형태로 출시되는 토큰들은 내장된 탈중앙화 거래소를 통해 블록체인 생태계의 이점을 누릴 수 있으며 오픈 소스 애플리케이션과 라이브러리를 통해 성공적인 개발, 자금 조달, 성장을 지원받을 수 있습니다. 
### 자발적인 사용자 층 확장을 위한 토큰 활용
---
스마트 미디어 토큰은 네트워크 사용자와 애플리케이션을 개발하는 기업 간의 인센티브를 조정하여 세계적인 콘텐츠 애플리케이션과 토큰을 연결짓는 획기적인 기술입니다. 스마트 미디어 토큰은 인플레이션의 개념(새로운 토큰 배출)과 글 작성 기반 보팅에 의한 토큰 할당 원칙을 적용하여, 콘텐츠 네트워크와 애플리케이션에 기여한 가치를 바탕으로 토큰을 분배합니다. 기업가는 이제 블로그, 애플리케이션, 혹은 애플리케이션과 주제에 대한 전체적인 네트워크에 통합할 수 있는 토큰을 생성할 수 있습니다. 스마트 미디어 토큰을 사용하면 기업가는 인플레이션율에서 토큰을 배분하는 알고리즘까지 제품에 통합되는 토큰의 경제성을 설정할 유연성을 확보할 수 있습니다.

스마트 미디어 토큰의 두 가지 고유한 특성 때문에 타 토큰(비트코인, 이더리움, ERC-20)과 인센티브 조정 방법에서 차이가 생기고, 스마트 미디어 토큰을 더 “똑똑하고 사회적”이게 만듭니다. 첫 번째는 콘텐츠 생성과 큐레이션(보상 풀)에 헌신적인 토큰 풀입니다. 두 번째는 집단 지성을 활용하여 콘텐츠의 가치를 평가하고 토큰을 분배하는 보팅 시스템입니다.이 두 가지 고유한 특성을 결합하여 창작 증명(Proof-of-Brain)이라 부르며, 이는 작업 증명에 기초하여 커뮤니티 참여자에게 토큰을 배분하는 과정에서 요구되는 사람의 노동력을 강조한 것입니다. 창작 증명을 이용하여 이용자 집단이 보상 체계가 갖추어진 커뮤니티에 가치를 더하도록 독려함으로써 커뮤니티의 점진적 성장을 추구합니다.

기업가와 설립 단체는 콘텐츠 네트워크를 성장시키기 위해 스마트 미디어 토큰을 사용합니다. 자동적이고 지속적으로 생성되는 새로운 토큰은 토큰 보유자들의 경쟁적인 보팅 과정을 통해 콘텐츠 생성자에게 분배됩니다. 토큰이 네트워크의 사용자들에게 분배될 때, 기존 토큰 보유자들은 콘텐츠 생성자, 애플리케이션 운영사, 서비스를 지원하는 사업가와 함께 이익을 나누어 갖습니다. 이같은 토큰의 특별한 경제적 특성은 새로운 사용자가 참여하도록 지속적인 인센티브를 제공하여 네트워크를 확대합니다. 기존 출판 사업자나 숨겨진 소셜 미디어 스타트업들은 자사 앱에 이 특별한 토큰을 통합하여 성장을 촉진할 수 있습니다.
### 새로운 자금 조달 기회
---
이더리움의  ERC20이 등장함에 따라 블록체인 기반 토큰들은 ICO(초기 코인 제공) 과정으로 조직에 투자금을 조달하는 새로운 수단으로 자리 매김하였습니다. ICO는 단체가 비공개적 또는 공개적으로, 특별한 목표를 위해, 영리적 또는 비영리적인 목적을 갖고 초기 토큰을 판매할 수 있는 기회를 제공합니다. 토큰이 판매되는 방식에 따라 여러 규제 기관에서 토큰을 상품, 유가 증권, 파생 상품, 또는 기타로 취급할 수 있습니다. 2017년에 ICO를 통해 모금된 투자금은 십억 달러를 상회하며, 이같은 흐름을 이어가기 위해 개발된 스마트 미디어 토큰의 ICO 스마트 컨트랙트로 편리하게 토큰을 출시 및 판매하는 것이 가능합니다. 스마트 미디어 토큰의 출시로 하드캡, 소프트캡, 캡이 설정되지 않은 ICO 모두 구축 가능하고, 스팀 및 타 암호화폐로 모금할 수 있습니다.
### 즉각적인 유동성
---
새롭게 설계된 시장 조성자 개념 [[2]](https://www.bancor.network/static/bancor_protocol_whitepaper_en.pdf)을 활용함으로써, 스마트 미디어 토큰 기반의 ICO는 스마트 미디어 토큰의 온 체인과 호가창의 시장 조성자에게 투자받은 스팀 토큰의 일정량을 전송하여 특정한 준비금 비율만큼의 유동성을 유지하도록 합니다. 스마트 미디어 토큰의 사회적 및 전문화된 분배 메커니즘을 넘어서, 이같은 특성은 참여자의 매도, 매수 주문이 활발하게 일어나는 분산화 시장으로 자동화된 시장 조성자의 개념을 발전시킵니다. 두 측면의 결합은 온 체인 및 무신뢰 거래를 가능하게 하는 동시에 토큰 사용자에게 유동성을 제공합니다. 
### 공유 부트스트랩 도구
---
스마트 미디어 토큰은 스팀 파워와 다른 스마트 미디어 토큰의 부여분 사이의 공유 영향력을 조절하는 [보상 풀](https://steem.io/steem-bluepaper.pdf) 변수와 함께 생성됩니다. 스마트 미디어 토큰 생성자는 스팀 파워가 스마트 미디어 토큰 보상 풀의 일부를 무제한 또는 제한된 시간 동안 영향력이 증가하거나, 감소하도록 제어할 수 있습니다. 종합하면, 공유 영향력은 스마트 미디어 토큰이 기존에 활동중인 스팀 또는 다른 스마트 미디어 토큰 커뮤니티 회원들의 관심에 의해 전체적 혹은 부분적으로 부트스트랩 되도록 허용할 수 있습니다. 이같은 도구를 사용하여 커뮤니티 매니저와 기업가가 토큰 출시를 하면, 기존 사용자 층을 기반으로 스마트 미디어 토큰을 목표 시장에 신속하게 배포할 수 있습니다. 
### 공유 토큰 보상을 통한 수익 창출
---
모든 스팀 기반의 인터페이스는 커뮤니티 매니저, 추천인, 기부 단체 등을 포함하는 임의의 수령인 집단 사이에 토큰 보상을 나눌 수 있는 옵션을 가지고 있습니다. 인터페이스는 작성자에게 토큰을 분할하는 방법에 대한 선택권을 제공합니다. 초기에 잠재적인 보상 공유 수혜자는 블록에 의한 소프트 캡에 의해 8명까지 책정되어 그 사용성을 입증했지만, 블록체인은 게시물 당 256명의 수혜자까지 추가하여 처리할 수 있습니다. 
### 저희 단체가 스마트 미디어 토큰에 참여할 수 있습니까?
---
스마트 미디어 토큰은 개인이나 단체에 의해 출시될 수 있습니다. 네트워크 사용료와 스팀 네임스페이스로 지불하기 위한 1 USD만 있다면 누구나 출시할 수 있습니다. [anon.steem.network](https://anon.steem.network/), [steemit.com](https://steemit.com), [steemconnect.com](https://v2.steemconnect.com/)을 비롯한 스팀 가입 서비스를 통해 등록할 수 있습니다.

토큰을 등록할 이름을 확보하고 나면, 사용자 계정은 스팀 기반의 커맨드 라인 도구나 미래에 출시될 토큰 출시 지원 도구를 통해 토큰을 발행할 수 있습니다. 토큰은 초기 판매나 토큰 분배를 지원하기 위해 설계될 수 있습니다. 인플레이션율과 같은 스마트 미디어 토큰의 특정한 속성은 토큰을 생성하는 개인이나 단체에 의해 정의되어야 합니다. 이같은 속성은 토큰이 어떻게 애플리케이션이나 각 공동체 속에서 사용될 지 규정합니다.

토큰 출시 이후 관련 사항은 블록체인에서 변경되지 않으며, 올바르게 활용될 때 이와 통합된 비즈니스의 성장은 토큰에 지대한 영향을 받게 됩니다.
### 사용 사례
---
실존하는 비즈니스와 미래의 기업가가 특수하게 설계된 스마트 미디어 토큰을 활용하여 인터넷을 변화시킬 5 가지 방법에 대하여 소개하겠습니다. 이러한 사례를 통해 애플리케이션 안에서 토큰을 설계하고 활용할 다른 방법을 발견할 수도 있습니다. 아래 목록은 모든 사례를 총망라하지 않으며, 새로운 사례가 가치를 입증하면 백서를 업데이트할 예정입니다.
#### 1 - 콘텐츠 게시자 - 단일 토큰 지원
주류 미디어 웹사이트의 성장 속도가 더뎌짐에 따라, 변화하는 기술 환경을 통해 앞서갈 방법을 모색합니다. 웹사이트는 “Disqus”와 유사한 스팀 기반 애플리케이션으로 마이그레이션 되거나 직접 스팀 API를 사용하여 통합합니다. 구독자가 댓글을 달면 암호화폐를 보상 받을 수 있습니다. 웹사이트를 준비하고 나면 댓글 인터페이스에를 통해 자사의 토큰 발행이 가능합니다. 토큰을 판매하여 자본 조달을 하거나 토큰을 이용해서 자율적 성장을 촉진할 수 있습니다.
![fig1](https://steemitimages.com/DQmQiCC8rfV6k5KsnPfiqvXQXhS88GzQDDDPu2xbq5Y2Cvx/contents_publisher.JPG)
그림 1: 단일 토큰 콘텐츠 게시자
#### 2 - 포럼 - 다중 토큰 지원
떠오르는 포럼 비즈니스는 암호화폐를 통합하여 현금 흐름을 창출하고, 다음 단계로 도약하고자 합니다. 하지만 이들은 암호화폐 보안 전문가가 아니며 암호화폐 지갑을 호스팅하고 있지도 않습니다. 대신 스마트 미디어 토큰을 발행하여 웹사이트에 통합할 수 있습니다. 포럼 비즈니스는 사회적 측면에만 온전하게 집중하고, 스팀커넥트와 같은 애플리케이션을 통합하여 지갑 및 전송 기능을 처리할 수 있습니다. 이를 통해 기업들은 암호화폐의 보안적 측면 대신 비즈니스의 성장(커뮤니티의 성장)만을 집중할 수 있게됩니다. 포럼은 특정 주제에 대한 토큰을 추가로 발행할 수 있습니다. 토큰 출시 권한은 웹사이트 운영사에 의해 관리되거나 웹사이트 커뮤니티 매니저에게 위임될 수 있습니다. 웹사이트의 특정 주제에 대한 토큰은 틈새 시장 전략으로 자율 성장을 촉진할 수 있습니다. 다중 토큰 모델과 관련한 웹사이트의 예시로는 ChainBB([chainbb.com](https://chainbb.com/forums))가 있습니다. 토큰은 도메인에서 전체적으로 사용할 수 있게 허용하거나, 특정 주제에 대한 커뮤니티에서 사용하도록 범위를 제한할 수 있습니다. 
![fig2](https://steemitimages.com/DQmRkBwmV5mhMP4uNAXMMssahyMERAp7xbVoLEGGJUvSGRh/forums.JPG)
그림 2: 다중 토큰 포럼
#### 3 - 온라인 게시자를 위한 댓글 위젯
온라인 게시자가 스마트 미디어 토큰을 자사 서비스에 신속히 통합하기 위한 방법은 WordPress나 Blogger와 같은 소프트웨어를 기반으로 구축된 기존 블로그에 쉽게 통합 가능한 스팀 기반 댓글 위젯을 사용하는 것입니다. 위젯을 사용하는 개발자는 댓글 작성자에게 분배되는 토큰 보상 중 일정량을 취득할 수 있습니다. 따라서 암호화폐 사용이 가능한 차세대 Disqus 같은 회사를 위한 비즈니스 기회를 창출합니다. 이를 통해 트랜잭션 서명 지원, 개인 키 관리, 지갑 기능, 게시자를 위한 호스팅 비용의 부담을 줄일 수 있습니다. 위젯 관리자에게 위와 같은 기능을 아웃소싱합니다.
![fig3](https://steemitimages.com/DQmeeZMzdKa4oLqqmQ41h33FFT8RfJBsXdKMSLUTJmMNcLg/comments_widget.JPG)
그림 3: 댓글 위젯
#### 4 - 하위 커뮤니티 사회자 및 매니저
Reddit의 “subreddit”이나 Steemit의 “community”와 같은 포럼에서 특정 주제의 사회자가 되었다고 상상해 봅시다. 만약 웹사이트를 특정 주제에 대한 스마트 미디어 토큰과 통합한다면, 사회자는 해당 주제의 구독자에게 힘을 주거나 자금 모금, 커뮤니티의 콘텐츠 큐레이션 질을 높이기 위해 토큰을 출시 할 수 있습니다. 
![fig4](https://steemitimages.com/DQmT7ugJAhhnsVrfdGCeU5LC5ZHbyjamsL1skHqAxNmNRem/moderators.JPG)
그림 4: 하위 커뮤니티
#### 5 - 임의 자산 - 실제 세계의 자산을 대표하는 토큰
기업가가 스팀 생태계에 유동성을 제공하고자 하는 사례에 대해 살펴봅시다. 기업가는 인플레이션 특성 없이 스마트 미디어 토큰을 발행할 수 있습니다. 또한 달러(또는 다른 부채, 계약, 자산)에 고정할 구조를 제공하거나 차용증서 또는 기본 파생 상품과 같은 것으로 만들 수 있습니다. 이같은 자산 제공 구조는 테더처럼 $1 부근에서 사고 파는 것이 포함됩니다. 기업가는 스위프트 같은 기능을 설정하여 구매 및 판매 과정에서 작은 수수료를 취할 수 있습니다. 파생 상품은 스팀과의 거래를 통해 모든 토큰에서 사용 가능하며, 이는 생태계에 자본을 가져다 줄 것입니다.
![fig5](https://steemitimages.com/DQma9PYAyncPiUpjVjnNLHgeyztEnsqehdeDTm7hQA2sFmy/arbitrary_asset.JPG)
그림 5: IOU 자산 토큰 거래소
## 소유자 매뉴얼
---
이 매뉴얼은 스마트 미디어 토큰의 작동 방식에 대한 기본적인 내용을 다룰 것입니다. 예상 독자는 직접 스마트 미디어 토큰을 생성하기를 원하는 기술자입니다.
### 통제 계정 생성
---
스마트 미디어 토큰을 생성하기 위한 첫 번째 단계는 통제 계정을 생성하는 것입니다. 어떤 스팀 계정이든 통제 계정의 역할을 수행할 수 있지만, 이를 위한 특수 목적의 계정을 새로 생성할 것을 권고합니다. 또한 새로 생성하는 계정은 글 작성, 보팅 및 스팀, 스팀 달러, 타 토큰 소유를 금할 것을 권장합니다(트랜잭션 대역폭 확보를 위한 소량의 스팀 파워는 제외). 

통제 계정의 이름은 유저 인터페이스에 있어서 큰 비중을 차지하지 않습니다. 따라서 스마트 미디어 토큰 브랜드에 적합하지 않게 작명하여도 상관이 없습니다.
#### 통제 계정의 보안
통제 계정의 보안은 출시 후 사용하는 사람에게 매우 중요합니다.
- 통제 계정은 2-of-3 또는 3-of-5의 다중 서명 보안을 사용하기를 권합니다.
- 통제 계정의 권한은 다중 서명 맴버로서 특정한 키를 갖지 않는 계정이 가져야합니다.
- 추가적인 보안을 위해서, 통제 계정의 다중 서명 그룹에 속한 각 계정 또한 다중 서명 보안을 사용해야합니다.
- 키들 중 일부는 오프라인으로 보관되야 합니다.
- 트랜잭션은 온라인 인터페이스를 통해 생성되야 하며, 이동식 매체를 통해 물리적 이동을 합니다.
- 서명은 UI를 통한 전송을 하기 위해 물리적 이동식 매체에서 온라인 시스템으로 반환되어야 합니다.

권한을 설정하고 나면, 계정이 여전히 거래 가능한 지 확인해야 합니다. 인증과 거래 서명을 설정할 때는 테스트넷에서 먼저 테스트 해보거나, 덜 중요한 계정으로 메인넷 네트워크를 사용해볼 것을 권장합니다.

토큰 출시 후, 계정의 키를 @null에게 할당해 소각하거나 동적 특성이 조정될 수 없게 만드는 방안을 고려해볼 수 있습니다.
#### 토큰 합의
토큰은 스팀을 포함하는 아토믹 트랜잭션을 하기 때문에 스팀 블록체인 합의의 일부를 고려하여 설계되었습니다.
### 토큰 생성과 초기화된 매개 변수
---
#### 스마트 미디어 토큰 객체 생성
첫 번 째로 실행될 작업은 `smt_creation_operation (smt 생성 작업)` 입니다. 이 작업은 블록체인 상태에 스마트 미디어 토큰 객체를 생성합니다. `smt_creation_operation`을 수행한 후에 새롭게 생성되는 스마트 미디어 토큰 객체는 온전히 구성되지 않은 상태입니다.

대부분의 구성은 후속 작업에서 이루어집니다(`smt_set_setup_parameters_operation (smt 설정 매개 변수 설정 작업)`, `smt_setup_inflation_operation (smt 인플레이션 설정 작업)`, `smt_setup_operation (smt 설정 작업)`). 이러한 후속 작업들은 동일 트랜잭션에서 수행될 수 있지만 차후에 수행될 수도 있습니다.
~~~
struct smt_create_operation
{
   account_name_type control_account;
   asset             smt_creation_fee;
   asset_symbol_type symbol;
   extensions_type   extensions;
};
~~~
#### 숫자 자산 식별자
스마트 미디어 토큰은 숫자 자산 식별자(numerical asset identifier, NAI)에 의해 참조됩니다. 2개의 ‘@’와 이어지는 9개의 숫자로 식별합니다(ex. `@@314159265`). 블록체인은 UI에 위치한  `smt_create_operation` 식별자가 원격 절차 호출 결과 `get_next_smt_identifier (다음 smt 식별자 가져오기)`의 값과 일치해야 한다는 것을 강제합니다. 따라서 스마트 미디어 토큰 생성자는 숫자 자산 식별자를 자유롭게 선택할 수 없습니다. 숫자 자산 식별자는 채굴 가능하지도 않으며 식별자 꾸미기(비트코인에서 사용하는 주소 꾸미기와 유사)도 가능하지 않습니다.

블록체인 설계자가 이 같은 제한을 두는 이유는 사용자들이 합의 수준 식별자를 상징 이름으로 사용하거나, 인간의 유의미한 상징을 식별자에 할당하여 비 합의 디렉토리 시스템을 이용하는 행위를 막기 위해서입니다. 블록체인은 브랜드의 합법적 소유자와 “네임 쿼터”를 구별할 수 없으며, 불법 복제자 스마트 미디어 토큰 생성 수수료를 지불할 의사가 있다면 더욱 구분이 어렵습니다.
#### 스마트 미디어 토큰 작명
이름 지정 문제에 대한 해결책은 숫자 자산 식별자를 이름으로 연결한 자산 디렉토리를 발행하는 것입니다. 자산 디렉토리는 합의 사항이 아니며, 블록체인 작동이 숫자 자산 식별자에 의해 직렬화 된다는 것을 의미합니다. 자산의 이름은 오직 유저 인터페이스상 표시를 위해 사용됩니다. 

유저 인터페이스는 파일, URL, 사용자 지정 디렉토리 항목을 게시하는 블록체인 계정과 같은 자산 디렉토리를 포함합니다. 자산 디렉토리의 게시자는 디렉토리 항목이 합법적인 브랜드 소유권 표준을 충족하고 있음을 보장해야 합니다.
#### 스마트 미디어 토큰 생성 수수료 
`smt_create_operation`를 발행하는 것은 `smt_creation_fee (smt 생성 수수료)` 지불을 필요로 합니다. `dynamic_global_properties_object (동적 전역 특성 객체)` 필드에 `smt_creation_fee` 지불시 필요한 금액이 지정되어 있습니다. 이 필드는 스팀 또는 스팀 달러의 가치로 표기될 수 있습니다. 만약 스팀 달러로 정해져 있다면, 현 시세 기준 동일 가치의 스팀 또한 허용이 가능합니다. 

초기 값으로 `smt_creation_fee`는 1 스팀 달러로 책정될 것이며, 이를 수정할 수단을 제공하지 않을 계획입니다. `smt_creation_fee` 비용은 미래에 하드포크를 할 때 수정될 수도 있기에, 유저 에이전트는 `dynamic_global_properties_object`에서 `smt_creation_fee` 값을 읽어와야 합니다. 유저 에이전트는 수수료가 항상 1 스팀 달러일 것이라 가정해서는 안되며, 인터페이스의 목적이 큐레이팅 된 토큰 집합을 사용하도록 설정하는 것이라면 별도의 수수료 정책을 준비해야 합니다. 

수수료는 `STEEM_NULL_ACCOUNT (스팀 null 계정)`에 전송함으로써 소각됩니다.
#### 스마트 미디어 토큰 사전 설정
두 가지 사전 설정을 위한 작업은 `smt_setup_inflation_operation`과 `smt_setup_parameters`를 포함합니다. 이 작업은 `smt_create_operation` 실행 후, `smt_setup_operation` 실행 전에 수행되야 합니다. 두 작업은 동일 트랜잭션에서 처리되거나 이전 블록에서 처리됩니다.

사전 설정 작업이 `smt_setup_operation` 작업의 일부가 아닌 이유는 여러 개의 블록에서 사전 설정 작업들이 처리될 수 있도록 허용하기 위해서 입니다.
#### 스마트 미디어 토큰 설정
각각의 스마트 미디어 토큰은 영구 구성 데이터를 갖는 기술자 객체를 가지고 있습니다. 이 데이터는 출시 후에는 수정할 수 없습니다. 기술자는 `smt_setup_operation`에 의해 설정됩니다.
~~~
struct smt_setup_operation
{
   account_name_type       control_account;
   asset_symbol_type       smt_name;
   int64_t                 max_supply = STEEM_MAX_SHARE_SUPPLY;
   smt_generation_policy   initial_generation_policy;
   time_point_sec          generation_begin_time;
   time_point_sec          generation_end_time;
   time_point_sec          announced_launch_time;
   time_point_sec          launch_expiration_time;
   extensions_type         extensions;
};
~~~
`smt_setup_operation`의 기호의 정밀도는 신뢰할 수 있습니다. 이전에 지정된 작업의 정밀도와는 다를 수 있으며 덮어 씌워질 수도 있습니다. 이후에 발행되는 작업은 대응되는 정밀도를 가져야 합니다. 

작업은 `control_account (통제 계정)` 키에 의하여 서명되야 합니다. 지명된 스마트 미디어 토큰은 `control_account`에 의해 먼저 생성되야 합니다. 기호에 포함된 소수 자릿수는 이전의 `smt_setup_operation` 과는 다를 수 있습니다.

유저 인터페이스에서 `decimal_places` 필드는 단위를 소수로 표시하는 데 사용됩니다.

`generation_begin_time`은 참여자가 ICO에 참여할 수 있는 시작 시간을 뜻합니다. 이를 통해 ICO 시작 전 참여자들은 ICO에 대해 연구할 시간을 가질 수 있습니다.

`generation_end_time`은 ICO 참여 종류 시간을, `announced_launch_time`은 ICO 토큰이 생성되는 시간을 의미합니다(ICO는 최소 모금액 수준을 넘어야 함). 

`generation_end_time` 과 `announced_launch_time` 사이에는 일시 중지 기능이 있어서 ICO 시작 후 공개되지 않은 히든 캡을 사용할 수 있게합니다. 이는 ICO 생성자가 출시 전 ICO 참여자의 최종 인원수를 파악할 시간을 줍니다.

`launch_expiration_time (출시 만료 시간)`에 ICO가 출시되지 않았다면, 모든 참여자는 자동적으로 환불받으며(가상 작업을 통해서) ICO는 취소됩니다. 상징은 특정 `control_account`에 영원히 보존됩니다. 하지만 토큰을 출시하기 위해서 `smt_create_operation`을 실행해야 하며 `smt_creation_fee`를 한 번 더 지불해야 합니다. 
#### 토큰 단위
초기 토큰 생성은 참여자로부터 받은 스팀 단위에 의해 결정됩니다. 반올림 문제를 무시하기 위해 투자금은 스팀 단위의 정수배여야 합니다. ICO 생성자는 스팀 단위를 책정합니다.
- 단위는 크든 작든 상관없습니다. 단위가 작을수록(ex. 1 STEEM 또는 0.1 STEEM)  ICO에 참여 가능한 사람들의 수가 증가하므로 작게 설정할 것을 권장합니다. 

스팀 단위는 토큰 출시 후 스팀 배분에 대한 라우팅 정책을 지정해야 합니다(요구에 따라 토큰 출시전 스팀을 환불 받을 수도 있습니다). 라우팅 정책에 따라 여러 명에게 스팀을 정해진 단위 만큼 분배하게 됩니다. 

ICO를 시작하면 토큰은 토큰 단위 만큼 생성됩니다. 모금한 스팀 단위 하나 당 여러 토큰 단위가 생성됩니다. 토큰 단위 또한 라우팅 정책을 갖습니다.
`smt_generation_unit (smt 생성 단위)` 구조에서 단위를 결정하고 라우팅 정책을 지정합니다. 
~~~
struct smt_generation_unit
{
   flat_map< account_name_type, uint16_t >        steem_unit;
   flat_map< account_name_type, uint16_t >        token_unit;
};
~~~
`flat_map`의 `(키, 값)` 쌍은 사토시의 라우팅을 결정합니다. 각 단위에 명시된 스팀/토큰 값의 합은 전체 가치의 합과 같습니다.
#### 단위 비율
스마트 미디어 토큰을 출시할 때, 스팀 단위에 대한 R-for-1 비율로 토큰 단위가 생성됩니다. 숫자 R은 단위 비율이라고 부릅니다.

`smt_generation_policy (smt 생성 정책)` 필드에서 `min_unit_ratio`와 `max_unit_ratio`에 허용 가능한 R값의 최대치와 최소치를 기입합니다. 

ICO에서 생성되는 토큰 단위 수의 최댓값은  ICO 생성자에 의해 결정되는 `max_token_units_generated (생성된 최대 토큰 단위 수)` 변수에 의해 제한됩니다(토큰은 출시 후에도 생성될 수 있지만, 차후에 생성되는 것은 인플레이션이라 부르고 이는 ICO에서 고려하지 않습니다). 

단위 비율은 실제로 모금한 스팀 단위에 대해 `max_token_units_generated`을 초과하지 않는 범위에 한해 가장 큰 정수 값으로 설정합니다. 
#### 캡과 최소값
ICO에서 최소 스팀 단위의 수 `min_steem_units`를 지정할 수 있습니다. 만약 ICO에서 `generation_end_time` 전까지 `min_steem_units`에 도달하지 못했다면 ICO는 성립되지 않으며, 참여자는 환불을 요구할 수 있습니다. 

마찬가지로 ICO에서 두 가지 최대 스팀 단위의 수(하드 캡과 소프트 캡)를 지정할 수 있습니다. 소프트 캡을 넘긴 단위에 대해서는 스팀과 토큰에 대해 다른 라우팅 정책을 적용합니다. 하드 캡을 초과할 때 받은 스팀 단위는 거부되며 이에 대한 스마트 미디어 토큰 또한 생성되지 않습니다.

소프트 캡은 모든 참여자에 대해 비율대로 분배하는 효과가 있습니다. 예를 들어 ICO의 소프트 캡이 8백만 스팀이었고, 10명의 참여자가 각각 1백만 스팀을 투자했다면 각각의 20만 스팀은 소프트 캡 정책에 따라 라우팅 됩니다. 

하드 캡은 마지막 참여자를 배제합니다. 예를 들어 ICO의 하드 캡이 8백만 스팀이었고, 10명의 참여자가 각각 1백만 스팀을 투자했다면 앞선 8명의 투자액은 온전하게 배정되며 마지막 2명은 1백만 스팀을 환불받게 됩니다.
#### 히든 캡
최소 캡과 하드 캡은 생성 정책 하에 숨겨질 수 있습니다. 이는 수치는 설정 시점에 고정되어야 하나 ICO 생성자가 값을 비밀로 부칠 수 있다는 것을 뜻합니다. 이 기능은 ***커밋/공개*** 암호화 프로토콜로 구현됩니다. ***commitment*** 라 불리는 해시는 설정 시간에 정해지며 실제 값은 약정과 일치해야 합니다(해시에는 논스가 포함되어 해커가 숨겨진 하드 캡을 찾기위해 브루트 포스 공격이나 추측을 통한 테스트 접근을 하는 것을 막을 수 있습니다).

스마트 미디어 토큰 설계자는 히든 캡의 값이 특정 범위 안에 있다는 사실을 사전에 공표하기를 바랄 수 있습니다. `lower_bound (하한)`와 `upper_bound (상한)` 필드는 명시된 값이 지정된 범위에 속한 값이 아닐 때 해시 불일치로 처리하는 기능을 합니다. 
~~~
struct smt_cap_commitment
{
   share_type            lower_bound;
   share_type            upper_bound;
   digest_type           hash;
};
struct smt_revealed_cap
{
   share_type            amount;
   uint128_t             nonce;
};
struct smt_cap_reveal_operation
{
   account_name_type     control_account;
   smt_revealed_cap      cap;
   extensions_type       extensions;
};
~~~
모든 캡은 숨겨져 있지만 특정 시점에는 공개되어야 합니다. 따라서 숨겨진 상한, 하한 값이 없는 ICO의 경우 `smt_cap_reveal_operation (smt 캡 공개 작업)` 작업과 `smt_setup_operation` 작업을 동일 트랜잭션에 포함하여 처리하면 됩니다. 사용자 인터페이스는 다음과 같은 기능을 합니다.

사용자 인터페이스는 `nonce(논스)`와 `amount(수량)` 값을 복구하기 위한 하나 이상의 수단을 제공해야 합니다. 
- `amount`와 `nonce`를 다시 입력하게 함으로써, 백업을 여부를 확인합니다.
- 결정론적 함수에 개인 키와 공개 키를 대입하여 `nonce` 값을 도출합니다. 예를 들어 `nonce = H(privkey + control_account + lower_bound + upper_bound + current_date)`.
- `nonce`가 공개되었을 때 불확실한 필드 값을 브루트 포스하기 위한 기능을 제공합니다. 예를 들어 현재 데이터 또는 `amount`를 제공합니다.
- `nonce`가 공개되었을 때 브루트 포스를 용이하게 하기 위해 `amount` 값을 낮은 엔트로피가 되도록 만듭니다. 예를 들어 1-999 사이의 숫자에 10의 거듭 제곱을 곱한 값을 사용합니다.
#### 정책 데이터 구조 생성
스마트 미디어 토큰의 생성 정책 데이터 구조는 다음과 같습니다. 
~~~
struct smt_capped_generation_policy
{
   smt_generation_unit pre_soft_cap_unit;
   smt_generation_unit post_soft_cap_unit;
   smt_cap_commitment  min_steem_units_commitment;
   smt_cap_commitment  hard_cap_steem_units_commitment;
   uint16_t            soft_cap_percent = 0;
   uint32_t            min_unit_ratio = 0;
   uint32_t            max_unit_ratio = 0;
   extensions_type     extensions;
};
~~~
`max_token_units_generated` 변수 값이 작업 코드 상 나타나지 않는다는 사실을 주목해 봅시다. 이 변수 값이 보이지 않는 이유는 다음과 같은 수식을 통해 유도 되었기 때문입니다. `max_token_units_generated = min_unit_ratio * hard_cap_steem_units`.

`smt_generation_policy`는 정적 변수로 정의되며, `smt_capped_generation_policy (smt 캡 생성 정책)`가 유일한 멤버입니다.
~~~ 
typedef static_variant< smt_capped_generation_policy > smt_generation_policy;
~~~
`typedef`는 미래 프로토콜 버전에서 다른 변수에 대해 추가적인 정책 의미 체계를 가질 수 있도록 허용합니다.
#### 예와 이론적 근거
##### ICO 예시
알파는 투자금을 모으기 위해 토큰을 판매할 계획을 가지고 있습니다. 투자받은 스팀의 70%는 알파 조직 계정(@alpha_org)으로, 23%는 설립자 계정 A(@founder_a)로, 7%는 설립자 계정 B(@founder_b)로 분배됩니다.

알파는 스팀 단위를 다음과 같이 정의합니다.
~~~
steem_unit = [["alpha_org", 70], ["founder_a", 23], ["founder_b", 7]]
~~~
스팀 단위는 100 스팀-사토시 또는 0.1 스팀입니다.

1 스팀을 기부받을 때마다, 알파의 기부자는 5 알파 토큰을 받으며, 설립자 계정 D는 1 알파 토큰을 받습니다. 이 ⅚, ⅙ 분배는 다음과 같이 표현됩니다.
~~~
token_unit = [["$from", 5], ["founder_c", 1]]
~~~
비율은 아래 데이터 구조와 같이 정의됩니다.
~~~
struct smt_generation_unit
{
   flat_map< account_name_type, uint16_t >        steem_unit;
   flat_map< account_name_type, uint16_t >        token_unit;
};
~~~
토큰 단위는 6 알파-사토시 또는 0.0006 알파 입니다(알파가 소수점 4자리까지 갖을 때).

***단위 비율*** 은 `steem_unit (스팀 단위)`이 기부될 때, `token_unit (토큰 단위)`이 발행되는 상대적인 비율로 정의합니다. 1 스팀 당 6 알파라는 명세를 맞추기 위해서, 1 스팀 단위 당 1000 알파 단위를 발행 합니다. 따라서 이 ICO의 단위 비율은 1000이 됩니다. `smt_capped_generation_policy` 데이터 구조에서 `min_unit_ratio (최소 단위 비율)`와 `max_unit_ratio (최대 단위 비율)` 필드는 다음과 같습니다.
~~~
min_unit_ratio = 1000
max_unit_ratio = 1000
~~~
특별한 계정 이름 `$from` 은 기부자를 의미합니다. `$from.vesting`은 `$from`의 귀속된 잔고를 의미합니다.
##### 왜 단위 비율을 사용합니까?
블록체인에서 간단하게 가격을 지정하는 대신 단위 비율을 사용하는 이유는 무엇입니까?

이유는 가격이 잘못 정의된 ICO 정의를 작성할 가능성이 있기 때문입니다. 예는 다음과 같습니다.
- `"$from"`은 `token_unit`에서 발생하지 않습니다.
- `"$from"`은 `token_unit`과 `token_unit`에서 발생합니다.
- `"$from"`과 `"$from.vesting"`의 조합이 발생합니다.
- 미래에 확장할 때, 새로운 특별 계정을 허용합니다.

모든 ICO 정의에서 단위 비율을 가지고 있으며, “가격”이라는 단일 수량을 정의하는 것은 이 같은 ICO에서 적용하기에 복잡하거나 불가능합니다.
##### 단위 비율의 사용자 인터페이스 처리
위에 대한 결과로 “ICO 가격” 개념은 순수하게 사용자 인터페이스 개념으로 사용됩니다. ICO 가격을 제공하는 사용자 인터페이스는 다음을 수행합니다.
- 사용자 인터페이스가 제공하는 “가격”의 정확한 정의를 문서화 합니다.
- 위와 같은 병적인 입력값에 대해서도 잘 동작해야 합니다.
- 단위 비율과 가격 표시를 전환할 수 있는 스위치 버튼을 제공합니다.
##### 히든 캡 FAQ
- Q: ICO는 특정 캡을 가져야만 하나요?
- A: 일부 사람들은 캡이 정해지지 않은 ICO를 “탐욕적”으로 인식하여 거부하거나, 그들이 기부하여 살 수 있는 ICO 비율에 대한 하한선을 보장받기를 원합니다. 

- Q: 캡은 숨겨져야만 하나요?
- A: 일부 사람들은 공개 캡이 투명하고 확실하길 바랍니다. 또 다른 사람들은 히든 캡이 흥분과 수요를 일으킬 것이라 생각합니다. 한 가지 가능한 타협은 10의 거듭제곱과 다음 거듭제곱 사이의 범위를 발표하는 것입니다. 예를 들어 ICO의 캡은 1 백만과 1 천만 스팀 사이로 발표할 수 있습니다.

- Q: 어떻게 캡을 비활성화 하나요?
- A: `STEEM_MAX_SHARE_SUPPLY (스팀 최대 지분 공급량)` 이상으로 캡을 설정하면 됩니다.
#### 출시
***효과적인 출시 시간*** 은 토큰 거래가 가능해진 시점입니다. 하드 캡을 공개하는 시간에 두 가지 가능성이 발생할 수 있습니다.
- `min_steem_units (최소 스팀 단위)`과 `hard_cap_steem_units (하드 캡 스팀 단위)`이 `announced_launch_time (출시 발표 시간)`시간 전에 공개되면, 정시 출시라고 부릅니다. 출시 로직은 사용자 행동에 상관없이 `announced_launch_time`시간이 되면 실행됩니다.
- `min_steem_units`과 `hard_cap_steem_units`이 `announced_launch_time` 시간 전에 공개되지 않으면, 지연 출시라고 부릅니다. 출시 로직은 `min_steem_units`과
 `hard_cap_steem_units` 이 공개되는 시점에 실행됩니다.
- 만약 출시가 지연된다면, `announced_launch_time`이 지난 시간 부터 출시 로직 실행 전까지 기부자는 스팀을 돌려받기 위해서 `smt_refund_operation (smt 환불 작업)` 작업을 실행할 수 있습니다.
이같이 설계한 이유는 다음과 같습니다.
- 히든 캡은 즉각적으로 발표되지 않습니다(이는 히든의 정의이기도 합니다).
- 히든 캡 공개는 ICO 생성자에 의해서만 이루어져야 합니다(비 공개적인 정보를 필요로 하는 모든 작업은 블록체인 위에서 자동적으로 수행될 수 없습니다).
- ICO 생성자가 작업을 하지 않으면 출시 로직은 절대 실행되지 않습니다.
- ICO 생성자가 악의적인 행동을 하거나 무응답 상태일 때는 기부자의 스팀은 영원히 갇히게 되며 어떠한 토큰도 받지 못하게 됩니다.
- 스팀이 갇히는 것을 막기 위해 `smt_refund_operation`이 고안되었습니다.
~~~
struct smt_refund_operation
{
   account_name_type       contributor;
   asset                   amount;
   extensions_type         extensions;
};
~~~
사용자는 `smt_refund_operation`을 사용할 필요가 없습니다. 기부자 개개인은 환불받기 위해 사전 동의를 해야합니다. 만약 ICO 생성자가 `announced_launch_time`전에 배포할 수 없는 합법적인 이유를 알리면, 모든 기부자는 자발적으로 `smt_refund_operation`를 사용하지 않도록 선택할 수 있습니다. 이 경우에 ICO 생성자가 숨겨진 값을 공개한 이후 출시가 진행됩니다.

출시 로직은 환불된 기여금은 기부 받지 않은 것으로 고려합니다. 따라서 출시 지연이 발생하였을 때, 각 기부자는 아래 두 가지 상태 중 하나를 선택할 수 있습니다.
 
- 기부자는 `smt_refund_operation`를 실행하여 스팀을 돌려받으며, ICO에 참여하지 않습니다다.
- 기부자는 환불을 요청하지 않고 그대로 ICO에 참여합니다.

출시가 지연되면 출시 예고 시점에 `min_steem_units`를 초과할 수 있으나, 기부자들이 환불을 요구하여 기부받은 스팀이 `min_steem_units`아래로 떨어질 수 있습니다. 이 같은 경우에 ICO는 성립하지 않으며 `min_steem_units`에 도달하지 못한 것으로 간주됩니다.
#### 전체적인 JSON 예시
##### 알파
이 예시는 앞서 살펴 보았던 알파의 ICO입니다. 이 ICO는 다음과 같은 특징을 가지고 있습니다.
- 기부받은 스팀의 70%는 알파 조직 계정으로 분배됩니다(@alpha_org). 
- 기부받은 스팀의 23%는 설립자 계정 A로 분배됩니다(@founder_a).
- 기부받은 스팀의 7%는 설립자 계정 B로 분배됩니다(@founder_b).
- 최소 기부 단위는 0.1 스팀입니다.
- 1 스팀을 기부받을 때마다 기부자는 5 알파를 분배 받습니다(@founder_a).
- 1 스팀을 기부받을 때마다 설립자 계정 C는 1 알파를 분배 받습니다(@founder_c).
- 최소값, 하드 캡, 소프트 캡이 없습니다.
- 출시 후에 인플레이션은 발생하지 않습니다.

![fig6](https://steemitimages.com/DQmQYnpcWbU2DN7mCXS8F5rjDqP1kFno1kD4QvSn8zCrjeT/alpha.JPG)
그림 6: 알파 ICO 흐름도

알파 토큰을 출시하기 위한 작업은 다음과 같습니다.
~~~
[
 ["smt_setup",
  {
   "control_account" : "alpha",
   "decimal_places" : 4,
   "max_supply" : "1000000000000000",
   "initial_generation_policy" : [0,
    {
     "pre_soft_cap_unit" : {
      "steem_unit" : [["alpha_org", 70], ["founder_a", 23], ["founder_b", 7]],
      "token_unit" : [["$from", 5], ["founder_c", 1]]
     },
     "post_soft_cap_unit" : {
      "steem_unit" : [],
      "token_unit" : []
     },
     "min_steem_units_commitment" : {
      "lower_bound" : 1,
      "upper_bound" : 1,
      "hash" : "32edb6022c0921d99aa347e9cda5dc2db413f5574eebaaa8592234308ffebd2b"
     },
     "hard_cap_steem_units_commitment" : {
      "lower_bound" : "166666666666",
      "upper_bound" : "166666666666",
      "hash" : "93c5a6b892de788c5b54b63b91c4b692e36099b05d3af0d16d01c854723dda21"
     },
     "soft_cap_percent" : 10000,
     "min_unit_ratio" : 1000,
     "max_unit_ratio" : 1000,
     "extensions" : []
    }
   ],
   "generation_begin_time" : "2017-08-10T00:00:00",
   "generation_end_time" : "2017-08-17T00:00:00",
   "announced_launch_time" : "2017-08-21T00:00:00",
   "smt_creation_fee" : "1.000 SBD",
   "extensions" : []
  }
 ],
 ["smt_cap_reveal",
  {
   "control_account" : "alpha",
   "cap" : { "amount" : 1, "nonce" : "0" },
   "extensions" : []
  }
 ],
 ["smt_cap_reveal",
  {
   "control_account" : "alpha",
   "cap" : { "amount" : "166666666666", "nonce" : "0" },
   "extensions" : []
  }
 ]
]
~~~
참고 사항:
- `soft_cap_percent (소프트 캡 백분율)`를 `STEEM_100_PERCENT = 10000` 로 설정함으로써 소프트 캡을 비활성화 합니다. 
- 소프트 캡이 비활성화 될 때 `post_soft_cap_unit (소프트 캡 단위 게시)` 값은 비어 있어야 합니다.
- 단위 비율은 수정되지 않으므로 `min_unit_ratio` / `max_unit_ratio` 는 고정됩니다.
- 논스를 0, `lower_bound == upper_bound`로 설정하여 히든 캡을 비활성화 합니다.
- `smt_cap_reveal_operation` 작업을 이용하여 캡을 공개해야 합니다.
- 지정된 하드 캡은 생성되는 토큰이 `STEEM_MAX_SHARE_SUPPLY`를 초과하지 않는 하드 캡입니다.
##### 베타
베타 토큰은 다음과 같은 규칙에 의해 생성됩니다.
- 5 스팀을 기부 받을 때마다 3 스팀이 설립자 계정 Fred에게 분배됩니다.
- 5 스팀을 기부 받을 때마다 2 스팀이 설립자 계정 George에게 분배됩니다.
- 초기 공급되는 토큰의 10%는 설립자 계정 George에게 분배됩니다.
- 초기 공급되는 토큰의 20%는 설립자 계정 Henry에게 분배됩니다.
- 초기 공급되는 토큰의 70%는 기부자들이 기부액에 따라 나누어 갖습니다.
- 스팀 단위는 0.005 스팀입니다.
- 토큰 단위는 0.001 베타 입니다.
- 최소 모금액은 5 백만 스팀 단위, 25,000 스팀입니다.
- 최대 모금액은 3 천만 스팀 단위, 150,000 스팀입니다.
- 기부자들은 최종 기부액에 따라 1 스팀 당 7~14 베타를 분배 받습니다.
- George는 최종 기부액에 따라 1 스팀 당 1~2 베타를 분배 받습니다.
- Harry는 최종 기부액에 따라 1 스팀 당 2~4 베타를 분배 받습니다.
- 만약 최대치인 3 천만 스팀 단위가 모금되었다면 `min_unit_ratio = 50`가 적용됩니다.
- 최대 토큰 단위의 수는 `min_unit_ratio` 곱하기 3 천만, 즉 15 억 토큰 단위 입니다.
- 각 토큰 단위가 0.001 베타이기 때문에 최대로 150만 베타 토큰이 생성될 수 있습니다.
- 만약 75,000 스팀 이하가 모금된다면 기부자, George, Harry는 각각 1 스팀 당 최대치인 14, 2, 4 베타를 분배 받습니다.
- 만약 75,000 스팀보다 많은 양이 모금된다면 기부자, George, Harry는 전체 공급량이 150 만 베타로 고정된 상태에서 70% / 10% / 20%를 분배 받습니다.
- 하드 캡의 결과에 따라 기부자, George, Harry는 기부 받은 1 스팀 당 적어도 7, 1, 2 개의 베타를 분배 받습니다.

이 예시는 비율이 어떻게 작동하는 지 보여주기 위해 선택되었습니다. 이는 현실적인 예시가 아니며, 대부분의 ICO는 알파와 같이 `min_unit_ratio = max_unit_ratio`로 설정하거나 베타처럼 큰 변수 값 `max_unit_ratio`를 선택할 것입니다.
~~~
[
 [
  "smt_setup",
  {
   "control_account" : "beta",
   "decimal_places" : 4,
   "max_supply" : "1000000000000000",
   "initial_generation_policy" : [0,
    {
     "pre_soft_cap_unit" : {
      "steem_unit" : [["fred", 3], ["george", 2]],
      "token_unit" : [["$from", 7], ["george", 1], ["henry", 2]]
     },
     "post_soft_cap_unit" : {
      "steem_unit" : [],
      "token_unit" : []
     },
     "min_steem_units_commitment" : {
      "lower_bound" : 5000000,
      "upper_bound" : 5000000,
      "hash" : "dff2e4aed5cd054439e045e1216722aa8c4758b22df0a4b0251d6f16d58e0f3b"
     },
     "hard_cap_steem_units_commitment" : {
      "lower_bound" : 30000000,
      "upper_bound" : 30000000,
      "hash" : "f8e6ab0e8f2c06a9d94881fdf370f0849b4c7864f62242040c88ac82ce5e40d6"
     },
     "soft_cap_percent" : 10000,
     "min_unit_ratio" : 50,
     "max_unit_ratio" : 100,
     "extensions" : []
    }
   ],
   "generation_begin_time" : "2017-06-01T00:00:00",
   "generation_end_time" : "2017-06-30T00:00:00",
   "announced_launch_time" : "2017-07-01T00:00:00",
   "smt_creation_fee" : "1000.000 SBD",
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "beta",
   "cap" : { "amount" : 5000000, "nonce" : "0" },
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "beta",
   "cap" : { "amount" : 30000000, "nonce" : "0" },
   "extensions" : []
  }
 ]
]
~~~
[이 스프레드시트](https://github.com/steemit/smt-whitepaper/blob/master/smt-manual/ico-parameters.ods)를 사용하면 관계를 명확히 알 수 있습니다.
##### 감마
감마 토큰은 베타 토큰과 비슷하나 한 가지 차이점이 있습니다. `max_unit_ratio` 변수는 ICO 초기에 최대 150 만개의 토큰이 발행된다는 것을 의미합니다. ICO는 150 만개의 감마 토큰을 효과적으로 기부자들에게 분배합니다(적어도 5개의 스팀을 기부해야 합니다).
 
~~~
[
 [
  "smt_setup",
  {
   "control_account" : "gamma",
   "decimal_places" : 4,
   "max_supply" : "1000000000000000",
   "initial_generation_policy" : [0,
    {
     "pre_soft_cap_unit" : {
      "steem_unit" : [["fred", 3], ["george", 2]],
      "token_unit" : [["$from", 7], ["george", 1], ["henry", 2]]
     },
     "post_soft_cap_unit" : {
      "steem_unit" : [],
      "token_unit" : []
     },
     "min_steem_units_commitment" : {
      "lower_bound" : 5000000,
      "upper_bound" : 5000000,
      "hash" : "dff2e4aed5cd054439e045e1216722aa8c4758b22df0a4b0251d6f16d58e0f3b"
     },
     "hard_cap_steem_units_commitment" : {
      "lower_bound" : 30000000,
      "upper_bound" : 30000000,
      "hash" : "f8e6ab0e8f2c06a9d94881fdf370f0849b4c7864f62242040c88ac82ce5e40d6"
     },
     "soft_cap_percent" : 10000,
     "min_unit_ratio" : 50,
     "max_unit_ratio" : 300000,
     "extensions" : []
    }
   ],
   "generation_begin_time" : "2017-06-01T00:00:00",
   "generation_end_time" : "2017-06-30T00:00:00",
   "announced_launch_time" : "2017-07-01T00:00:00",
   "smt_creation_fee" : "1000.000 SBD",
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "gamma",
   "cap" : { "amount" : 5000000, "nonce" : "0" },
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "gamma",
   "cap" : { "amount" : 30000000, "nonce" : "0" },
   "extensions" : []
  }
 ]
]
~~~
##### 델타
이 ICO에서 1 백만 델타 토큰이 설립자를 위해 생성되며 기부자에게 할당되는 토큰은 없습니다. 설립자를 포함하여 모든 사용자는 0.1개의 스팀 기부를 통해 토큰 생성을 시작할 수 있습니다.
~~~ 
[
 [
  "smt_setup",
  {
   "control_account" : "delta",
   "decimal_places" : 5,
   "max_supply" : "1000000000000000",
   "initial_generation_policy" : [0,
    {
     "pre_soft_cap_unit" : {
      "steem_unit" : [["founder", 1]],
      "token_unit" : [["founder", 10000]]
     },
     "post_soft_cap_unit" : {
      "steem_unit" : [],
      "token_unit" : []
     },
     "min_steem_units_commitment" : {
      "lower_bound" : 10000000,
      "upper_bound" : 10000000,
      "hash" : "4e12522945b8cc2d87d54debd9563a1bb6461f1b1fa1c31876afe3514e9a1511"
     },
     "hard_cap_steem_units_commitment" : {
      "lower_bound" : 10000000,
      "upper_bound" : 10000000,
      "hash" : "4e12522945b8cc2d87d54debd9563a1bb6461f1b1fa1c31876afe3514e9a1511"
     },
     "soft_cap_percent" : 10000,
     "min_unit_ratio" : 1000,
     "max_unit_ratio" : 1000,
     "extensions" : []
    }
   ],
   "generation_begin_time" : "2017-06-01T00:00:00",
   "generation_end_time" : "2017-06-30T00:00:00",
   "announced_launch_time" : "2017-07-01T00:00:00",
   "smt_creation_fee" : "1000.000 SBD",
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "delta",
   "cap" : { "amount" : 10000000, "nonce" : "0" },
   "extensions" : []
  }
 ],
 [
  "smt_cap_reveal",
  {
   "control_account" : "delta",
   "cap" : { "amount" : 10000000,  "nonce" : "0" },
   "extensions" : []
  }
 ]
]
~~~
##### 베스팅 기부금
즉각적인 유동성을 확보하는 대신, 부분 또는 전체 기부금을 베스팅 잔고로 옮기는 것이 가능합니다. 예제에서는 95%를 베스팅 잔고로 옮겼습니다.
~~~
"token_unit"           : [["$from.vesting", 95], ["$from", 5]]
~~~
##### 기부된 스팀 소각
이 ICO에서 스팀은 사람의 지갑으로 들어가지 않고 영원히 파괴됩니다. 이는 상대 ICO의 구조를 모방한 것입니다.
~~~
{
 "steem_unit" : [["null", 1]],
 "token_unit" : [["$from", 1]]
}
~~~
##### 비용으로써의 베스팅(스팀 파워)
이 ICO에서는 토큰을 얻기 위해 발행자에게 스팀을 전송할 필요가 없습니다. 대신 스팀을 자기 자신한테 귀속하면, 귀속된 스팀과 동등한 양의 토큰이 발행됩니다.
~~~
{
 "steem_unit" : [["$from.vesting", 1]],
 "token_unit" : [["$from", 1]]
}
~~~
##### 스팀 외의 코인과 하이브리드 ICO
스팀 달러, 비트코인, 이더리움 등 스팀 이외의 코인을 ICO에 사용하는 경우 온 체인에서 완전히 자동으로 수행할 수 없습니다. 그러나 이러한 ICO는 설립자 계정에서 구매자의 스팀 계정으로 기여분 만큼을 수동으로 전송하여 관리할 수 있습니다. 
#### 인플레이션 매개 변수
스마트 미디어 토큰 출시 이후 생성되는 것을 ***인플레이션*** 이라고 부릅니다.

인플레이션은 기여자가 가치를 제공한데에 따른 스마트 미디어 토큰의 보상입니다.

인플레이션 이벤트는 다음과 같은 데이터 구조를 따릅니다.
~~~
struct smt_inflation_unit
{
   flat_map< account_name_type, uint16_t >        token_unit;
};
// Event:  Support issuing tokens to target at time
struct token_inflation_event
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;
   uint32_t            num_units;
};
~~~
이 이벤트는 스마트 미디어 토큰 단위 `num_units (단위 수)`를 출력합니다.
#### 가능한 인플레이션 목표
목표는 인플레이션이 향하는 개체 입니다. 목표는 일반적인 개인 설립자의 스팀 계정 또는 여러 설립자들로 구성된 다중 서명 보안 계정입니다.

또한 블록체인 자체에서 제공하는 무신뢰 함수로 표현되는 몇몇 특수 대상일 수도 있습니다. 
- 보상: 토큰의 게시 / 보팅 보상을 나타내는 특수 대상
- 베스팅: 베스팅 된 토큰을 지원하는 토큰을 나타내는 특수 대상
#### 이벤트 순서
블록체인은 전통적으로 블록 단위로 인플레이션을 계산합니다. 이는 블록 생산 보상이 인플레이션의 주요(종종 또는 유일한) 수단이기 때문입니다.

하지만, 스마트 미디어 토큰을 위해 블록 생성을 하는 결합된 인플레이션을 진행할 이유가 없습니다. 사실 스마트 미디어 토큰은 블록을 가지고 있지 않기 때문에(블록 생성을 하는 기본 기능은 스팀으로 보상받는 스팀의 증인들이 공급합니다) 블록 보상을 가지지 않습니다.

일정한 간격으로 발생하는 인플레이션은 `token_inflation_event (토큰 인플레이션 이벤트)` 데이터 구조에 `interval_seconds (초 단위 간격)`과 `interval_count (간격 횟수)`를 추가하여 활성화 할 수 있습니다. 이에 대한 결과는 `token_inflation_event_seq_v1`라 불리는 새로운 데이터 구조입니다.
~~~
// Event seq v1:  Support repeatedly issuing tokens to target at time
struct token_inflation_event_seq_v1
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;
   asset               new_smt;
   int32_t             interval_seconds;
   uint32_t            interval_count;
};
~~~
데이터 구조는 토큰 인플레이션 이벤트가 매 `interval_seconds` 초 마다, `interval_count` 번 발생한다는 것을 뜻합니다. 최대 정수 값은 `0xFFFFFFFF`로 이벤트 시퀀스가 영원히 반복됨을 의미하는 경계값 입니다.

`new_smt (새로운 smt)`는 단위 수가 아닌 스마트 미디어 토큰의 수량 입니다. 단위 수는 `new_smt`를 전체 `unit` 멤버의 합으로 나눈 값으로 결정됩니다. 
#### 상대적인 인플레이션을 추가하기
인플레이션 일정은 종종 절대적인 용어가 아닌 공급 비율로 표현됩니다.
~~~
// Event seq v2:  v1 + allow relative amount of tokens
struct token_inflation_event_seq_v2
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;
   uint32_t            num_units;
   int32_t             interval_seconds;
   uint32_t            interval_count;
   asset               abs_amount;
   uint32_t            rel_amount_numerator;
};
~~~
공급원으로부터 `new_smt`를 계산합니다.
~~~
rel_amount = (smt_supply * rel_amount_numerator) / SMT_REL_AMOUNT_DENOMINATOR;
new_smt = max( abs_amount, rel_amount );
~~~
만약 `SMT_REL_AMOUNT_DENOMINATOR (smt 상대적인 양의 분모)` 값을 2의 거듭 제곱의 수로 표현 한다면 나눗셈은 비트 이동 연산을 통해 최적화될 수 있습니다. 비트에서 더 동적인 범위를 얻기 위해, 시프트를 변수화할 수 있습니다.
~~~
// Event seq v3:  v2 + specify shift in struct
struct token_inflation_event_seq_v3
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;
   int32_t             interval_seconds;
   uint32_t            interval_count;
   asset               abs_amount;
   uint32_t            rel_amount_numerator;
   uint8_t             rel_amount_denom_bits;
};
~~~
계산 과정은 다음과 같습니다. 
~~~
rel_amount = (smt_supply * rel_amount_numerator) >> rel_amount_denom_bits;
new_smt = max( abs_amount, rel_amount );
~~~
위 연산시 중간 값인 `smt_supply (smt 공급) * rel_amount_numerator (상대적인 양의 분자)` 에서 나타날 수 있는 잠재적인 오버플로우 문제를 조심해야 합니다.
#### 시간 변조 추가
시간 변조는 부분 선형 함수를 이용해 시간에 따라 연속적으로 변하는 인플레이션을 구현할 수 있게 합니다. 이는 단순히 시간 간격의 왼쪽과 오른쪽에 끝점을 지정하고 각각에 절대 값을 지정하여 얻을 수 있습니다.
~~~
// Event seq v4:  v3 + modulation over time
struct token_inflation_event_seq_v4
{
   timestamp           schedule_time;
   smt_inflation_unit  unit;
   int32_t             interval_seconds;
   uint32_t            interval_count;
   timestamp           lep_time;
   timestamp           rep_time;
   asset               lep_abs_amount;
   asset               rep_abs_amount;
   uint32_t            lep_rel_amount_numerator;
   uint32_t            rep_rel_amount_numerator;
   uint8_t             rel_amount_denom_bits;
};
~~~
이와 관련한 사항들
- 상대적인 값의 분자들만 보간되고, 양 끝점의 분모는 동일합니다.
- 왼쪽 끝점 이전의 시간에서는 왼쪽 끝점에서의 값이 사용됩니다.
- 오른쪽 끝점 이후의 시간에서는 오른쪽 끝점에서의 값이 사용됩니다.

코드는 다음과 같습니다.
~~~
if( now <= lep_time )
{
   abs_amount = lep_abs_amount;
   rel_amount_numerator = lep_rel_amount_numerator;
}
else if( now >= rep_time )
{
   abs_amount = rep_abs_amount;
   rel_amount_numerator = rep_rel_amount_numerator;
}
else
{
   // t is a number between 0.0 and 1.0
   // this calculation will need to be implemented
   // slightly re-arranged so it uses all integer math
   t = (now - lep_time) / (rep_time - lep_time)
   abs_amount = lep_abs_amount * (1-t) + rep_abs_amount * t;
   rel_amount_numerator = lep_rel_amount_numerator * (1-t) + rep_rel_amount_numerator * t;
}
~~~
#### 인플레이션 동작
인플레이션은 다음과 같이 동작합니다.
~~~
struct smt_setup_inflation_operation
{
   account_name_type   control_account;
   timestamp           schedule_time;
   smt_inflation_unit  inflation_unit;
   int32_t             interval_seconds = 0;
   uint32_t            interval_count = 0;
   timestamp           lep_time;
   timestamp           rep_time;
   asset               lep_abs_amount;
   asset               rep_abs_amount;
   uint32_t            lep_rel_amount_numerator = 0;
   uint32_t            rep_rel_amount_numerator = 0;
   uint8_t             rel_amount_denom_bits = 0;
   extensions_type     extensions
};
~~~
`setup_inflation_operation`은 `smt_setup_operation`을 수행하기 전에 실행 되야하는 사전 설정 작업입니다. 사전 설정 작업 섹션을 참조하시기 바랍니다.
#### 인플레이션 FAQ
- Q: 스마트 미디어 토큰의 인플레이션 데이터 구조가 [현 스팀의 인플레이션 설계](https://github.com/steemit/steem/issues/551)를 따릅니까?
- A: 네(반올림 에러는 제외).
- Q: 스마트 미디어 토큰의 인플레이션 데이터 구조가 X 달/년 후 설립자에게 직접적인 보상을 줄 수 있습니까?
- A: 네.
- Q: 시간 변조를 신경쓰고 싶지 않다면, 비활성화할 수 있습니까?
- A: 네. `lep_abs_amount == rep_abs_amount`, `lep_rel_amount_numerator == rep_rel_amount_numerator` 같이 동일 값으로 설정하고 `lep_time = rep_time`으로 설정합니다. 
- Q: 이같은 복잡성이 잘 설계된 사용자 인터페이스에 의해 가려질 수 있습니까? 
- A: 네.
- Q: 완벽한 정확도를 가진 시간 함수로 인플레이션을 모델링할 수 있습니까?
- A: 인플레이션 데이터 구조는 완벽하게 모델링되고 시뮬레이션할 수 있습니다. 다만 발행 구조는 기부금의 크기에 따라 발행양이 달라질 수 있기 때문에 완벽한 정확성을 갖는 구조를 설계하지 못할 수 있습니다.
#### 명명된 토큰 매개 변수
스팀의 일부 동작은 `steemd`의 C++ 소스 코드에 있는 `#define` 문에 의해 구현되는 구성 상수의 영향을 받습니다. 이와 같이 스마트 미디어 토큰 생성자는 스마트 미디어 토큰에 대해 동등한 동작을 하도록 구성할 수 있어야 합니다.

매개 변수는 `runtime_parameters (실행 시간 매개 변수)`와 `setup_parameters (설정 매개 변수)`입니다. `setup_parameters`는 `smt_setup_operation`의 필드입니다. 반드시 `smt_setup_operation` 작업 실행 전에 설정되야 하며, 한 번 실행된 이후에는 변경할 수 없습니다.

`runtime_parameters`는 `smt_set_runtime_parameters_operation (smt 실행 시간 매개 변수 설정 작업)`에 있는 필드로 토큰 생성자에 의해 수정될 수 없습니다.

다음 동작은 아래와 같이 정의되어 있습니다.
~~~
struct smt_set_setup_parameters_operation
{
   account_name_type                                 control_account;
   flat_set< smt_setup_parameter >                   setup_parameters;
   extensions_type                                   extensions;
};
struct smt_set_runtime_parameters_operation
{
   account_name_type                                 control_account;
   flat_set< smt_runtime_parameter >                 runtime_parameters;
   extensions_type                                   extensions;
};
~~~
현재 `setup_parameters`와 `runtime_parameters`는 다음과 같이 정의됩니다.
~~~
struct smt_param_allow_vesting                    { bool value = true;  };
struct smt_param_allow_voting                     { bool value = true;  };
typedef static_variant<
   smt_param_allow_vesting,
   smt_param_allow_voting
   > smt_setup_parameter;
struct smt_param_windows_v1
{
   uint32_t cashout_window_seconds = 0;              // STEEM_CASHOUT_WINDOW_SECONDS
   uint32_t reverse_auction_window_seconds = 0;      // STEEM_REVERSE_AUCTION_WINDOW_SECONDS
};
struct smt_param_vote_regeneration_period_seconds_v1
{
   uint32_t vote_regeneration_period_seconds = 0;    // STEEM_VOTE_REGENERATION_SECONDS
   uint32_t votes_per_regeneration_period = 0;
};
struct smt_param_rewards_v1
{
   uint128_t               content_constant = 0;
   uint16_t                percent_curation_rewards = 0;
   uint16_t                percent_content_rewards = 0;
   curve_id                author_reward_curve;
   curve_id                curation_reward_curve;
};
struct smt_param_allow_downvotes
{
   bool value = true;
};
typedef static_variant<
   smt_param_windows_v1,
   smt_param_vote_regeneration_period_seconds_v1,
   smt_param_rewards_v1,
   smt_param_allow_downvotes
   > smt_runtime_parameter;
~~~
이같은 매개 변수를 검사하고 설정하는 사용자 인터페이스는 각 매개 변수의 타입과 스케일을 확인해야 합니다. 특별히 백분율 매개 변수는 1/100% 스케일(예를 들어 100%는 다음과 같이 표현 됩니다. `STEEM_100_PERCENT = 10000`)로, 사용자 인터페이스와 다른 트랜잭션 생성 및  검사 도구는 ***반드시*** 1/100% 스케일을 사용해야 합니다.
### 매개 변수 상수
---
토큰 사용자에게 해를 입힐 가능성이 있는 몇몇 동적 매개 변수는 악용되는 것을 막기 위해 제한되야 합니다. 
- `0 < vote_regeneration_seconds < SMT_VESTING_WITHDRAW_INTERVAL_SECONDS`
- `0 <= reverse_auction_window_seconds + SMT_UPVOTE_LOCKOUT < cashout_window_seconds < SMT_VESTING_WITHDRAW_INTERVAL_SECONDS`
### 스마트 미디어 토큰 베스팅의 의미론
---
스마트 미디어 토큰은 스팀과 비슷한 베스팅 의미론을 갖고 있습니다.
- 스마트 미디어 토큰은 베스팅 잔고에 “파워 업”할 수 있습니다.
- 스마트 미디어 토큰의 베스팅 잔고는 13주에 걸쳐 “파워 다운”할 수 있습니다(정적 변수 `SMT_VESTING_WITHDRAW_INTERVALS (smt 베스팅 인출 간격)`와 `SMT_VESTING_WITHDRAW_INTERVAL_SECONDS (smt 베스팅 인출 초 단위 간격)`를 통해 통제됩니다).
- 보팅은 파워 업된 토큰에 의해서만 영향을 받습니다.
- 베스팅 잔고는 전송 불가이며 판매할 수 없습니다.

추가적으로 일부 토큰 인플레이션이 베스팅 잔고에서 발생하게 할 수 있습니다. 새롭게 발행된 토큰은 사용자들이 베스팅 잔고에 저장한 수량에 비례하여 효율적으로 분배되게 됩니다. 발행되는 토큰의 수는 사용자의 베스팅 잔액과는 독립적이기 때문에 분배 받는 비율은 그 시점에 저장된 전체 토큰 수에 전적으로 의존합니다.  
### 콘텐츠 보상
---
새롭게 생성되는 스마트 미디어 토큰은 보상 기금으로 유입됩니다. 블록체인은 다음을 결정하기 위한 알고리즘을 사용합니다.
- (1) 어떻게 게시물 간의 토큰 보상을 분배할 것인가.
- (2) 어떻게 게시글의 작성자와 큐레이터(업보터) 사이의 보상을 분배할 것인가.

이같은 문제를 해결하기 위한 알고리즘은 다음과 같은 작업을 수행합니다.
- (1) 게시물의 보상은 보상 곡선(`rc`)에 따라 다른 게시물에 대한 가중치를 반영합니다.
- (2a) 큐레이터들은 `curation_pct` 변수에 의해 정해진 고정된 비율 만큼 게시글 보상을 가져갑니다.
- (2b) 저자는 남은 보상을 가져갑니다(모든 수혜자와 제한/거부 게시글의 저자 보상을 취합한 후에 적용됩니다). 
- (2c) 큐레이터의 보상은 큐레이션 곡선(`cc`)에 따라 다른 큐레이터에 대한 가중치를 반영합니다.

![fig7](https://github.com/steemit/smt-whitepaper/blob/master/smt-manual/img/creation.png)
그림 7: 초기 토큰과 스마트 토큰 발행의 흐름
### 곡선 정의
---
보상 곡선은 선형 또는 이차 함수로 정의됩니다. 선형 보상 곡선은 `rc(r) = r` 식에서 R(업보트)값을 변경하지 않고 전달합니다. 이차 보상 곡선은 `rc(r) = r^2 + 2rs` 식으로 증가하는 기울기를 갖습니다.

보상 곡선의 의미를 설명하기 위해 가장 업보트가 많이된 게시물들을 묶어서 생각해봅시다.
- 섹션 A에는 보팅 기준 상위 10%에 해당하는 게시글들이 모여 있습니다.
- 섹션 B에는 다음 상위 10%에 해당하는 게시글들이 모여 있습니다.

보상은 다음과 같이 달라지게 됩니다.
- 각 곡선에 대해 섹션 A는 섹션 B보다 많은 업보트를 받았기 때문에 더 큰 보상을 받습니다.
- 이차 보상 곡선에서 섹션 A는 섹션 B보다 단위 업보트 당 보상이 더 크기 때문에 추가적으로 더 많은 보상을 받습니다.
- 선형 보상 곡선에서 섹션 A와 섹션 B는 단위 업보트 당 보상이 동일합니다.

가능한 큐레이션 곡선은 다음과 같습니다.
 
- 선형 `cc(r) = r`
- 제곱근 `cc(r) = sqrt(r)`
- 유계 `cc(r) = r / (r + 2s)`

시각화를 돕기 위해 파이 차트를 보여드리겠습니다. 색깔이 칠해진 각각의 영역은 동일한 보팅 파워에 대해 큐레이션 보상이 어떻게 분배되는지 표현합니다.

![fig8](https://github.com/steemit/smt-whitepaper/blob/master/smt-manual/img/rc-cc.png)

그림 8: 보상 곡선과 큐레이션 곡선
- 직사각형 수직 열은 업보트를 할 때의 즉각적인 보상을 의미합니다.
- 오른쪽으로 확장된 색칠 영역은 나중에 큐레이터가 보팅을 할 때 보상이 어떻게 커지는지를 보여줍니다.
- 선형 곡선에서는 어떤 게시물에 보팅했는지에 관계없이 동일한 보상을 받습니다.
- `rc_linear + cc_sqrt`과 `rc_quadratic + cc_bounded`의 경우 같은 높이의 직사각형은 모든 이가 동일한 초기 큐레이션 보상을 받는다는 것을 의미하며 이를 `ICR=`라 부릅니다.
- `rc_linear + cc_bounded`의 경우 직사각형의 높이가 감소합니다. 이미 유명해진 게시물에 보팅할수록 불이익을 받는다는 것을 의미하며 이를 `ICR-`라 부릅니다.
- `rc_quadratic + cc_sqrt`와 `rc_quadratic + cc_linear`의 경우 직사각형의 높이는 증가하며, 이를 ICR+라 부릅니다.

근본적으로 큐레이션은 미래의 업보트에 대한 예측을 하는 것입니다. 시스템 설계자로서 보상 곡선의 선택 기준은 성공적인 예측에 대한 보상이어야 합니다. 어떤 곡선이 이같은 기준을 충족할지는 현재와 미래 업보트 사이의 관계에 달려있습니다.
- 만약 게시글의 미래 업보트가 현재 업보트들에 대해 독립적이게 만들려면 `ICR= `곡선을 선택해야 합니다.
- 만약 게시글의 미래 업보트가 현재 업보트들과 양의 상관관계를 갖도록 만들려면 이상적으로 상관관계의 양을 조절하는 `ICR-` 곡선을 선택해야 합니다.
- 만약 게시글의 미래 업보트가 현재 업보트들과 음의 상관관계를 갖도록 만들려면 이상적으로 상관관계의 양을 조절하는 `ICR+` 곡선을 선택해야 합니다.

실용적으로 독립성 또는 보통의 양의 상관관계를 위해 `ICR=`이나 `ICR-` 곡선을 선택합니다. 스팀의 경우 큐레이션의 보상 곡선은 2차 함수 `ICR=`였으나 하드포크 19 이후 선형 함수 `ICR=` 곡선을 적용하고 있습니다.
### 일일 목표 보팅
---
각각의 계정은 0%에서 100%까지 고정 비율로 채워지는 “마나 바”인 `voting_power (보팅 파워)`를 가지고 있습니다.

비율은 다음 두 가지 매개 변수에 의해 결정됩니다.
- (a) 바의 게이지가 100%까지 재충전되기 위한 시간은 `vote_regeneration_period_seconds`입니다.
- (b) 최대 힘을 갖는 보팅에 의해 `voting_power`가 이용됩니다.
`vote_regeneration_period_seconds`를 직접 지정합니다. (b)에서 최대 힘을 갖는 보팅의 보팅 파워를 직접 지정하는 대신에 `votes_per_regeneration_period`를 지정합니다. 사용자가 최대 힘을 갖는 보팅을 남발하면 재생산이 취소되도록 제한합니다.
### 스마트 미디어 토큰 설정의 GUI 스케치
---
![fig9](https://steemitimages.com/DQmVSDk3iheEhJBPiwGTuMfE7TA4SzCrZKi76nmbTt97DUk/setup.JPG)
그림 9: 스마트 미디어 토큰 구성 요소
### 유권 및 보상 가능성
---
이번 섹션에서는 유권과 보상 가능성에 대한 개념을 소개하겠습니다.
- 해당 토큰 잔액이 댓글에 영향을 줄 수 있다면 토큰은 투표권을 갖습니다.
- 댓글에 보팅 가능한 토큰으로 업 보트를 하면 보상을 받거나 권고할 수 있습니다.
- 보상을 받을 수 있는 토큰은 댓글 보상에 영향을 줄 수 있습니다.
- 만약 토큰이 권고하는 용도로 사용된다면 해당 토큰의 보팅은 댓글 보상에 영향을 끼치지 않습니다.

자문용 보팅은 보상 또는 보팅 파워에 영향을 받지 않습니다. 하지만 순위 알고리즘과 예상 보상 계산은 여전히 자문용 보팅을 포함하기 때문에 사용자 인터페이스는 자문 게시글을 표시할 수 있습니다.

보팅 가능한 토큰의 집합은 `allowed_vote_assets`(`comment_options_extension`, 댓글 옵션 확장 코드)에 의해 결정됩니다.
~~~
struct allowed_vote_assets
{
   flat_map< asset_symbol_type, votable_asset_info >      votable_assets;
};
struct votable_asset_info_v1
{
   share_type        max_accepted_payout    = 0;
   bool              allow_curation_rewards = false;
};
typedef static_variant< votable_asset_info_v1 >           votable_asset_info;
~~~
토큰의 보팅 가능 여부를 결정하는 규칙은 아래와 같습니다.
- 스팀은 모든 게시물에 대해 보팅 가능합니다.
- 토큰이 게시물의 `votable_assets`에 표시된다면 보팅할 수 있습니다.
- 그렇지 않다면, 토큰은 게시물에 보팅할 수 없습니다.

토큰이 보상 받을 수 있는 지를 판단하는 규칙은 아래와 같습니다.
- 게시글에 대한 보상을 받기 위해서는 토큰이 게시글에 보팅 가능해야 합니다.
- 게시물의 `max_accepted_payout`이 0인 경우 토큰은 해당 게시물에 보상을 줄 수 없습니다.
- 만약 보터(업보터/다운보터)의 토큰 잔액이 0이라면, 보터의 보팅은 보상 효력이 없습니다.
- 만약 스팀이 아닌 토큰의 `max_accepted_payout`이 0이 아니라면 스팀 또는 스팀 달러에 대한 `max_accepted_payout`은 적어도 `max_accepted_payout` 이상이어야 합니다.

구현 노트: 
- 자문 보팅의 경우, 큐레이터와 수혜자 모두 받을 수 있는 보상은 0입니다. 이는 블록체인이 큐레이터/수혜자 계산을 하기 전에 `max_accepted_payout`캡을 적용하기 때문입니다.
- 현재(스팀 하드포크 19) 스팀 블록체인은 자문 보팅에 대한 보팅 파워를 공제하지 않습니다. 이는 다음 스팀 하드포크(스팀 이슈 #1380)에서 수정될 예정입니다.
- 최대 두 개의 토큰이 `votable_assets`에 지정될 수 있습니다. 이는 각각의 게시물이 최대 3개의 토큰으로부터 보팅받을 수 있음을 의미합니다(스팀 포함).
- `max_accepted_payout`의 기본 값은 `dynamic_global_properties_object`의 멤버인 `max_accepted_steem_payout_latch`에 저장됩니다. 미래 버전에서 기본 값의 변화가 생긴다면 사용자는 멤버를 기반으로 한 게시물의 `max_accepted_payout`를 채워 넣어야 합니다.

어떤 합의 수준의 제한도 특정 게시물이 특정 `allowed_vote_assets`를 갖도록 강제하지 않습니다. 따라서 모든 게시물은 어떤 토큰으로도 보상 받을 수 있음을 표시할 수 있습니다. 하지만 사용자 인터페이스는 `allowed_vote_assets`에 있는 합의 되지 않은 유효성 검증 규칙을 강제하거나 그들의 합의 되지 않은 유효성 검증 규칙을 침해하는 게시물을 숨길 수 있습니다.

예를 들어 토큰을 사용하는 하이브마인드 커뮤니티에는 커뮤니티 내의 게시물에 지정된 `allowed_vote_assets`은 해당 커뮤니티의 토큰을 포함해야 한다는 유효성 검증 규칙이 있을 수 있습니다. 하이브마인드 커뮤니티 내에 존재하는 게시물의 전체적인 개념은 합의되지 않은 개념이기 때문에 이는 합의 되지 않은 유효성 검사 규칙입니다. 합의 되지 않은 유효성 검사이기 때문에 어떤 합의 로직도 이를 강제할 수 없습니다. 하지만 하이브마인드 커뮤니티를 인식하는 사용자 인터페이스는 이 유효성 검증 규칙을 위반하는 게시물의 색인 생성과 표시를 거부할 수 있습니다.
### 정적 토큰 매개 변수
---
정적 매개 변수는 스마트 미디어 토큰의 동작에 영향을 주는 구성 상수지만, `smt_setup_parameters`과 `smt_runtime_parameters`는 의도적으로 제외됩니다. 구성 가능하지 않게 설계한 이유는 매개 변수가 스팀에서 사용된 값에서 크게 벗어나게 허용하면 다음과 같은 심각한 위험을 초래할 수 있기 때문입니다.
- 매우 복잡한 구현을 초래할 수 있습니다.
- 최종 사용자에게 좌절감을 안길 수 있습니다.
- 토큰의 보안성과 안정성을 위협할 수 있습니다.
- 스팀의 보안성과 안정성을 위협할 수 있습니다.

정적 매개 변수의 목록은 아래와  같습니다.
- `SMT_UPVOTE_LOCKOUT_HF17 (smt 업보트 잠금 하드포크 17)` : 정적 -- 이 값은 현금 인출 이전 특정 시간에 다운 보트
 남용을 막기 위해 업보트 기능을 제한합니다.
- `SMT_VESTING_WITHDRAW_INTERVALS (smt 베스팅 인출 간격)` : 정적
- `SMT_VESTING_WITHDRAW_INTERVAL_SECONDS (smt 베스팅 인출 초 단위 간격)` : 정적
- `SMT_MAX_WITHDRAW_ROUTES (smt 최대 인출 경로)` : 정적
- `SMT_SAVINGS_WITHDRAW_TIME (smt 저금액 인출 시간)` : 정적
- `SMT_SAVINGS_WITHDRAW_REQUEST_LIMIT (smt 저금액 인출 요청 제한)` : 정적
- `SMT_MAX_VOTE_CHANGES (smt 최대 보팅 기회)`: 정적
- `SMT_MIN_VOTE_INTERVAL_SEC (smt 최소 보팅 초 단위 간격)` : 정적
- `SMT_MIN_ROOT_COMMENT_INTERVAL (smt 최소 루트 댓글 간격)` : 정적
- `SMT_MIN_REPLY_INTERVAL (smt 최소 댓글 간격)` : 정적
- `SMT_MAX_COMMENT_DEPTH (smt 최대 댓글 깊이)` : 정적
- `SMT_SOFT_MAX_COMMENT_DEPTH (smt 소프트 맥스 댓글 깊이)` : 정적
- `SMT_MIN_PERMLINK_LENGTH (smt 최소 허용 링크 길이)` : 정적
- `SMT_MAX_PERMLINK_LENGTH (smt 최대 허용 링크 길이)`: 정적
### 의무적인 토큰 매개 변수
---
`smt_setup_parameters`과 `smt_runtime_parameters`에 의해 설정되는 토큰 매개 변수는 기본 값을 갖습니다. 몇몇 스팀 등가 매개 변수는 `smt_setup_operation` 필드에 의해 지정됩니다. 이러한 매개 변수는 기본 값을 갖지 않으며 매 자산마다 직접 지정 되어야 합니다.
- `SMT_MAX_SHARE_SUPPLY (smt 최대 지분 공급)` : `smt_setup_operation.max_supply`에 의해 설정됩니다.
- `SMT_BLOCKCHAIN_PRECISION (smt 블록체인 정확도)` : `pow(10, smt_setup_operation.decimal_places)`에 의해 설정됩니다.
- `SMT_BLOCKCHAIN_PRECISION_DIGITS (smt 블록체인 정확도 자릿수)` : `smt_setup_operation.decimal_places`에 의해 설정됩니다.
### 스마트 미디어 토큰과 기존 작업의 상호 작용
---
- `comment_payout_beneficiaries (댓글 지불금 수혜자들)` : 기존 `comment_payout_beneficiaries` 는 스팀만을 재전송 합니다. 미래에 스마트 미디어 토큰도 재전송하는 `comment_payout_beneficiaries` 기능을 추가할 것입니다.
- `comment_options (댓글 옵션)` : `max_accepted_payout (최대 허용 지불금)`, `allow_votes (허용 보팅)`는 오직 스팀에만 영향을 줍니다. 자산에 대한 `max_accepted_payout`을 제한하려면 여기를 참조하세요. `allow_curation_rewards (허용 큐레이션 보상)`는 모든 토큰에 영향을 끼칩니다.
- `vote_operation (보팅 작업)` : 댓글에 투표 가능한 다중 여러 토큰들의 집합.
- `transfer_operation (전송 작업)` : 스마트 미디어 토큰을 지원합니다.
- `Escrow operations (에스크로 작업)` : 스마트 미디어 토큰을 지원하지 않습니다.
- `transfer_to_vesting_operation (베스팅으로 전송하는 작업)` : 베스팅을 지원하는 모든 스마트 미디어 토큰을 지원합니다.
- `withdraw_vesting_operation (베스팅 인출 작업)` : 베스팅을 지원하는 모든 스마트 미디어 토큰을 지원합니다.
- `set_withdraw_vesting_route_operation (베스팅 인출 경로 설정 작업)` : 스마트 미디어 토큰을 지원하지 않습니다.
- `account_witness_vote_operation (계정 증인 투표 작업)` : 스마트 미디어 토큰은 증인 투표에 영향을 주지 않습니다.
- `account_witness_proxy_operation (계정 증인 프록시 설정 작업)` : 스마트 미디어 토큰은 증인 투표에 영향을 주지 않습니다.
- `feed_publish_operation (피드 게시 작업)` : 스마트 미디어 토큰을 위한 피드가 게시되지 않을 수 있습니다.
- `convert_operation (전환 작업)` : 스마트 미디어 토큰은 전환 불가합니다.
- `Limit order operations (제한 주문 작업)` : 스팀에 대한 스마트 미디어 토큰의 거래는 제한 주문 기능을 지원합니다.
- `transfer_to_savings_operation (저금으로 전송하는 작업)` : 스마트 미디어 토큰은 저금 기능을 지원합니다.
- `decline_voting_rights_operation (투표 권한 거부 작업)` : 스팀 보팅 뿐만 아니라 스마트 미디어 토큰의 보팅에도 영향을 끼칩니다.
- `claim_reward_balance_operation (보상금 잔액 청구 작업)` : 이 작업에 대한 제한 사항은 스마트 미디어 토큰을 포함하는 세 가지 필드 중 하나에 자산을 허용하도록 완화 되었습니다.
- `delegate_vesting_shares_operation (베스팅 지분 위임 작업)` : 베스팅을 지원하는 모든 스마트 미디어 토큰을 지원합니다.
- `Multisig Native (고유 다중 서명) ` : 다중 서명으로 서명된 스마트 미디어 토큰 작업을 처리하는 것은 그다지 특별하지 않습니다. 만약 계정의 다중 서명 보안 기능을 사용한다면, 계정으로 서명할 때마다 지정된 다중 서명을 사용해야 합니다. 여기에는 스마트 미디어 토큰을 관리하는 통제 계정과 토큰을 보유한 일반 사용자가 수행하는 작업이 모두 포함됩니다.
## 스마트 미디어 토큰을 위한 자동화된 시장 조성자
---
자동화된 시장 조성자는 [Bancor 프로토콜 [2]](https://www.bancor.network/static/bancor_protocol_whitepaper_en.pdf)에 큰 기반을 둔 스마트 컨트랙트로 스마트 미디어 토큰 커뮤니티에 영원한 유동성을 공급하기 위해 초기 ICO 설정 과정 중 구성됩니다. 간단하게 설명하면, 스팀의 자동화된 시장 조성자는 오직 스팀과 다른 스마트 미디어 토큰과의 거래할 수 있습니다.
### 설정
---
#### 기본 정의
이 글에서 STEEM의 수량은 s로, 토큰(SMT)의 수량은 t로, 가격은 p로 표기할 것입니다. pt는 STEEM으로의 가치를 의미합니다(ex. MYTOKEN 한 개당 0.05 STEEM과 상응하고 p = 0.05 STEEM / MYTOKEN, MYTOKEN이 120개가 있다면 t = 120, 스팀으로의 가치 pt = 0.05 STEEM / MYTOKEN * 120 MYTOKEN = 6 STEEM 입니다).

두 가지 자산 s STEEM과 t 토큰을 운용하는 투자자에 대해 생각해봅시다. 토큰의 가격이 t라면 STEEM으로의 포트폴리오 자산 가치는 v(p, s, t) = s + pt가 됩니다.

한 가지 일반적인 포트폴리오 운영 정책으로는 포트폴리오에 STEEM을 일정 비율 r로 유지시키는 방법이 있습니다(s = rv(p, s, t), 0 < r < 1). 이러한 정책을 고정 포트폴리오 비율 정책(CPR 정책)이라 부르며 s = rv(p, s, t)는 CPR에 대해 불변합니다.

Bancor 백서에 기술된 다른 포트폴리오 운영 정책으로는 고정 준비금 비율 정책(CRR 정책)이 있습니다. CRR을 설명하기 위해 해당 토큰의 존재하는 전체 수량을 T로 표시하면, s = rv(p, 0, T-t)가 됩니다(해당 식은 CRR에 불변).
#### 규칙에 대한 서술
스마트 미디어 토큰 백서가 Bancor 백서와는 다르게 해석하는 부분에 대하여 서술하고자 합니다. Alice라는 고객이 시장 조성자와 거래한다고 할 때, Alice는 계좌 잔고에서 자신이 갖고 있는 토큰을 일정 수량 제거하는 대신에 상대방의 STEEM을 받을 것입니다. 반대로 Bob은 STEEM을 판매한 대가로 Alice로 부터 토큰을 받아 잔고에 더하게 됩니다.

위와 같은 예제에서 Bancor는 다음과 같은 규칙을 사용합니다. 시장 조성자는 Alice와 거래하는 과정에서 해당 토큰을 파괴하고, Bob과 거래하는 과정에서 해당 토큰을 생성합니다. Bancor의 규칙은 시장 조성자가 일반적인 행위자가 아닌 시스템 레벨에 해당하는 ‘특별한 힘’이 있다는 것을 시사합니다(거래시 토큰을 발행하는 특별한 권리를 갖고 있다고 볼 수 있음).

스마트 미디어 토큰 백서에서는 토큰 거래시 Alice가 보낸 토큰을 파괴하는 것이 아니라 시장 조성자의 계좌 잔고에 더하는 것으로, Bob 또한 새로 생성되는 토큰을 받는 것이 아니라 이미 존재하는 토큰을 시장 조성자로부터 넘겨 받는 것으로 해석합니다. 따라서 시장 조성자는 ‘특별한 힘’을 가질 필요가 없이 결정적인 알고리즘에 의해 거래하는 일반적인 거래 참여자가 됩니다.
### 유한 거래
---
#### 기본 정의 
거래시 (s, t) -> (s + Δs, t + Δt)로 시장 조성자의 잔고가 변합니다. 거래가 일어나는 순간의 가격은 p = Δs/Δt 로 정의됩니다. 올바른 거래의 조건은 Δs = Δt = 0 또는 Δs과 Δt값이 모두 0이 아니고 부호가 다른 수인 경우입니다다.

이론: 가격 p 에서의 거래는 가격 p의 가치를 보존합니다. 엄밀히 말하면 만약 Δs와 Δt가 가격 p인 거래를 의미한다면 v(p, s, t) = v(p, s + Δs, t + Δt)가 성립한다는 것을 의미합니다.

더욱 엄밀히 시장 조성자를 튜플 M = (s, t, T, r)로 정의합니다. 주어진 p 값에 대해 복원 거래(완화 거래 또는 완화)는 가격 p에서 일어난 CRR 불변을 만족하는 거래로 정의합니다. 
#### 복원 거래 계산
복원 거래는 Δs(M, p)와 Δt(M, p)의 함수를 포함합니다. 가격과 CRR 불변 정의로부터 이 함수들을 계산할 수 있습니다.

![eq1](https://steemitimages.com/DQmbGG9ze38jAZUjuzoGB8UeRstCvV4mLgjvhc7TuM7QYtn/computing_restoring_trade.JPG)
#### 평형 가격 계산
상태 M에 대하여, 복원 거래가 0일 때의 어떤 가격 Peq(M)가 존재합니다. 이를 평형 가격이라 부릅니다. Δs = 0 으로 두어 평형 가격을 계산할 수 있습니다.

![eq2](https://steemit-production-imageproxy-upload.s3.amazonaws.com/DQmYgjd8QtUy2TVJ2ynGyLWysHSPQg4XBjqwMRwqR3v4Dem)

이론: 완화는 멱등수 입니다. 즉 가격 p에서 완화된 후 결과 상태의 가격은 p이며, 두 번째로 가격 p에서 완화되면 0 거래가 됩니다.
#### 예제
예제: M = (1200, 3600, 12000, 0.25),  p = 0.5이라 가정합시다. T = 12000 개의 토큰이 존재하고, MM은 t = 3600 개의 토큰을 소유합니다. 그러면 T-t = 12000 - 3600 = 8400 개의 토큰이 순환합니다(MM의 계좌 밖에 존재). 시장에 유통되는 토큰의 가치는 p(T-t) = 4200 스팀이며 이는 목표 보존 수준인 rp(T-t) = 4200 * 0.25 = 1050 스팀에 의해 보증 됩니다.

이 예에서 너무 많은 스팀이 준비금으로 예치되기 때문에 완화는 시장에서 토큰을 구매해야 합니다. 이 판매로 인해 두 가지 효과가 발생합니다. 이는 스팀 준비금을 감소시키며 시장에 유통되는 토큰의 수를 줄어들게 합니다. 유통되는 토큰 량의 감소는 목표 준비금의 수준을 감소시킵니다. 토큰을 구매하기 위해 사용되는 1 스팀마다 목표 준비금 수준은 r 스팀만큼 감소됩니다. r < 1 이기 때문에 감소하는 준비금은 천천히 감소하는 목표 수준을 따라잡을 것입니다.
위의 대수학으로 아래 식을 얻을 수 있습니다.

![eq3](https://steemitimages.com/DQmQwaNmt5DWjxe8nVFeMv6GPikfANYZN6zausyUtUHeFby/algebra.JPG)

이 예에서 정의한 수들을 계산하면 Δs = -200 스팀, Δt = 400 토큰 값을 없을 수 있습니다. 계산된 Δs = -200, Δt = 400 값(a)은 가격 0.5에서의 거래를 의미하고, (b) CRR 불변은 새로운 상태 M_new = (s + Δs, t + Δt, T, r) 값을 갖습니다. p = Δs/Δt 를 계산하면 p = 0.5값을 구할 수 있습니다. 이 거래가 모두 성사된 이후, 시장 조성자는 s_new = s + Δs = 1200 - 200 = 1000 스팀, t_new = t + Δt = 3600 + 400 = 4000 토큰 값을 가지게 됩니다.
CRR 불변이 갖는 (b) 조건을 확인하기 위해, 이 예제의 첫 단락에서 초기 값을 새로운 값으로 바꾸어 반복해 보겠습니다. M_new = (1000, 4000, 12000, 0.25), p = 0.5 입니다. T = 12000 개의 토큰이 존재할 때, MM이 t_new = 4000 개의 토큰을 소유한다면 유통되는 토큰의 수 T-t_new = 12000 - 4000 = 8000 입니다. 유통되는 토큰의 가치 p(T-t_new) = 4000 스팀이며, 이는 목표 준비금 수준인 rp(T-t) = 4000 * 0.25 = 1000 스팀에 의해 보증되야 합니다. 목표 준비금 수준이 실제 준비금 수준인 s_new = 1000 스팀과 일치하기 때문에 CRR 불변이 완화 거래 이후에도 만족된다는 것을 알 수 있습니다.
### 극소 거래
---
이번 섹션에서는 상당히 기술적인 내용을 다룰 것입니다. 독자는 미적분과 미분 방정식에 대한 좋은 이해가 있어야 결과를 도출하는 과정을 따라갈 수 있을 것입니다.
#### 문제 설정
가격 p = p_eq 에서 불변 조건을 만족한다고 가정해봅시다. CRR 불변에 의해 s = rv(p, 0, T-t) = rp(T-t)가 됩니다. 또한 가격이 p + Δp로 증가하고 완화 거래 Δs, Δt가 새롭게 형성된 가격에서 일어난다고 가정해봅시다.

이번 섹션에서 Δp가 무한히 작은 제한적 상황을 가정하며 라이프니츠 표기법(p의 작은 변화를 dp, s의 작은 변화를 ds, t의 작은 변화를 dt로 표기)을 이용할 것입니다.
#### 미분 방정식의 해법
p를  p + dp로 치환하고, 지난 섹션에서 계산한 ds에 대한 식을 이용하면 분리 가능한 미분 방정식을 얻어 간단히 하여 풀어낼 수 있습니다.
![eq4](https://steemitimages.com/DQmb6UXu8EvzJQc8qdmohvrFEZhmthyrrAfHTcwzhrZ57xp/de.JPG)
이와 유사하게 t에 대하여도 dt = -ds/p로부터 분리 가능한 미분 방정식을 풀어낼 수 있습니다.
![eq5](https://steemitimages.com/DQma7YU6ctDv3JM8NVDD7KWi37NuS85rkuriPcGximANxZ4/de2.JPG)
### 질적인 분석
---
CRR 시장 조성자에 대하여 새롭게 발행되는 토큰은 어디에서 오는 것일까?

한 가지 옵션은 준비금 비율 r을 낮추는 것입니다. 이 옵션은 시장 활동에 즉각적인 영향을 끼치지 않지만 시장 조성자의 미래 가격 변동에 대한 대응을 취약하게 만들 수 있습니다. 이를 후불 옵션이라 부릅니다.

다른 옵션은 동적 시스템의 초기 조건을 변경하는 것입니다. 예를 들어 통합 상수를 수정하는 방법이 있습니다. 이 옵션을 사용하면 평형 가격 p가 떨어져서 시장 조성자는 토큰을 구매하여 준비금을 채워넣어야 합니다. 만약 매수 호가창의 매물이 토큰 발행량보다 많고 충분한 수의 토큰 매수 대기자가 있다면, 판매를 통해 준비금을 채워넣고 예전 가치에 가까운 평형 가격을 유지할 수 있을 것입니다. 두터운 매수 호가창은 시장 조성자가 주도하는 가격 변동에 대한 저항성을 키우게 됩니다. 만약 매수 호가창의 매물이 토큰 발행량보다 적고 토큰의 매수 대기자들이 적다면, 평형 가격이 하락하여 시장 가격을 낮추게 됩니다. 만약 매우 적은 토큰만이 판매되거나 준비금으로 예치되어 있는 스팀의 절대량이 이전과 거의 같아진다 하여도, 낮아진 토큰의 시가 총액에 대한 준비금의 상대적인 가치는 준비금 비율만큼 높아지게 됩니다. 이를 즉시 지불 옵션이라 부릅니다.  
### FAQ
---
- Q: 고정 포트폴리오 비율 정책과의 관련성은 무엇입니까?
- A: 미래에 시장 조성자 정책 지원을 받게될 수 있습니다.
- Q: 준비금 비율이 100%를 넘어설 수 있습니까?
- A: 없습니다.
- Q: 준비금 비율이 100%에 근사할 수 있습니까?
- A: 백서에서 기술된 시스템 속에는 존재하지 않지만, 특수한 경우 코딩이 가능합니다.
- Q: CRR 시장 조성자에게 있어 새롭게 발행되는 토큰은 어떻게 보증받을 수 있습니까?
- A: 블록체인 설계자는 보증에 대한 두 가지 옵션을 제공합니다. 한 가지 옵션은 준비금 비율 r을 낮추는 것입니다. 이 옵션은 시장 활동에 즉각적인 영향을 끼치지 않지만 시장 조성자의 미래 가격 변동에 대한 대응을 취약하게 만들 수 있습니다. 이를 후불 옵션이라 부릅니다.
다른 옵션은 동적 시스템의 초기 조건을 변경하는 것입니다. 예를 들어 통합 상수를 수정하는 방법이 있습니다. 이 옵션을 사용하면 평형 가격 p가 떨어져서 시장 조성자는 토큰을 구매하여 준비금을 채워넣어야 합니다. 만약 매수 호가창의 매물이 토큰 발행량보다 많고 충분한 수의 토큰 매수 대기자가 있다면, 판매를 통해 준비금을 채워넣고 예전 가치에 가까운 평형 가격을 유지할 수 있을 것입니다. 두터운 매수 호가창은 시장 조성자가 주도하는 가격 변동에 대한 저항성을 키우게 됩니다. 
만약 매수 호가창의 매물이 토큰 발행량보다 적고 토큰의 매수 대기자들이 적다면, 평형 가격이 하락하여 시장 가격을 낮추게 됩니다. 만약 매우 적은 토큰만이 판매되거나 준비금으로 예치되어 있는 스팀의 절대량이 이전과 거의 같아진다 하여도, 낮아진 토큰의 시가 총액에 대한 준비금의 상대적인 가치는 준비금 비율만큼 높아지게 됩니다. 이를 즉시 지불 옵션이라 부릅니다.  

- Q: 지불 중단 옵션은 어디에 있습니까?
- A: 새롭게 발행되는 토큰을 누가 보증하는 지 생각해 보아야 합니다. 발행되는 토큰이 없거나 토큰에 대한 보증이 없지 않다면 말입니다. 따라서 지불 중단 옵션은 발행되는 스마트 미디어 토큰이 없거나 시장 조성자가 없을 경우 존재합니다.
- Q: 분수 지수는 부동 소수점 구현을 필요로 합니까?
- A: 매우 높은 정밀도, 비트 단위의 컴파일러, OS, CPU 등의 재현성, 거대한 수에 대한 빠른 연산을 요구하는 경우에만 고려할 필요가 있습니다(백서 저자는 고려하고 있지 않습니다). 빠른 연산, 근사치 계산, 모든 정수에 대한 적용 모두 가능합니다.
- Q: 시장 조성자는 기존의 한도 주문 시스템을 통해서 호가창을 관리합니까? 아니면 별도로 운영하고 있습니까?
- A: 이론적으로 두 가지 방법 모두 구현이 가능합니다. 하지만 코드의 모듈화를 위해 시장 조성자와 시장의 호가창을 분리하여 구현할 가능성이 높습니다. 실제로 완벽하게 구분된 서브 시스템을 구현한다면, 사람들은 준비금 시스템과 기존 시장 시스템 사이에서 발생하는 가격 차이를 취하기 위한 차익 거래 봇을 운영할 수 있을 것입니다.
- Q: 시장 조성자의 초기 토큰 잔액은 어디에서 나옵니까?
- A: ICO 단위는 시장 조성자를 목적지로 지정할 수 있습니다. ICO 생성자는 ICO로 기부받은 스팀의 일정량을 설립자 계좌로 전송하는 것처럼 시장 조성자 MM에게 직접적으로 전송할 수 있습니다. 또는 소프트 캡을 적용해 일정 ICO 목표액을 초과하는 스팀을 시장 조성자에게 분배할 수 있습니다. 이와 마찬가지로 ICO 모금액 중 고정된 비율의 토큰을 MM의 토큰 잔액으로 할당할 수 있습니다.
- Q: 누구나 스팀 또는 토큰을 시장 조성자에게 전송할 수 있습니까?
- A: 네.
- Q: 스팀 또는 토큰을 시장 조성자에게 전송할 때 발생할 수 있는 부작용은 무엇입니까?
- A: 통합 상수가 다시 초기화되어 평형 가격이 변경 됩니다. 시장 조성자는 자산 매각에 대해 더욱 공격적인 성향을 띠게 됩니다.
- Q: 시장 조성자의 재고를 개인적인 이익을 위해 조작하거나 지출할 수 있습니까?
- A: 시장 조성자에게 자산을 전송하면 거래 활동에 참여하게 되어 가격에 영향을 줄 수 있습니다. 하지만 같은 양을 시장에 투매하면 가격에 훨 씬 더 큰 영향을 끼치게 됩니다. 만약 Eve가 시장 조작을 하기 위해 그녀의 토큰/스팀을 전송할 계획을 갖고 있다면, 비용 효율이 높은 시장에 바로 투매하는 전략을 선택할 것입니다.
- Q: 시장 조성자의 활동이 이익(또는 손해)을 냅니까?
- A: 이는 이익을 어떻게 측정하는 지에 따라 갈리게 됩니다. 만약 스팀과 토큰의 가치를 US 달러, 비트코인과 같은 외부 제 3의 화폐로 측정한다면 명확히 증가하거나 감소할 수 있습니다. 만약 사람들이 자발적으로 스팀 또는 토큰을 시장 조성자에게 전송한다면, 위 같은 가치 측정 방법과 관계없이 시장 조성자의 자산 가치가 증가하게 됩니다. 
또 다른 이익 평가 방법은 통합 상수를 이용하는 것입니다. 만약 양쪽의 통합 상수가 증가하거나, 한 쪽은 증가하나 다른 한 쪽은 일정하게 유지될 때 시장 조성자는 “테이커” 모드로서 각 거래마다 작은 이익을 취할 수 있습니다.

- Q: “테이커” 모드는 무엇입니까? 어떻게 시장 조성자가 “테이커” 모드로 작동하게 설정할 수 있습니까?
- A: 주문을 처리할 때 가격을 지정해 두는 주문을 메이커라고 부릅니다. 메이커의 반대말이 테이커 입니다. 스팀 온체인 시장(거의 모든 거래 플랫폼에서도 동일)에서는 오래된 주문은 항상 메이커 입니다.
시장 조성자가 테이커 모드일 때, 모든 거래 행위는 상대방이 지정한 가격을 구매하는 시장가 주문으로 간주됩니다. 이 가격은 시장 조성자가 받아들일 의사가 있는 것보다 조금 더 후한 값입니다. 시장 조성자가 테이커 모드가 아닐 때, 모든 거래 행위는 통합 상수를 변하게 만들지 않는 지정가 주문으로 간주됩니다.
테이커 모드는 스마트 미디어 토큰의 통제 계정에 의해 설정되는 실행 시간 매개 변수 입니다.
- Q: 누가 시장 조성자의 테이커 모드로 이익을 얻습니까?
- A: 아무도 아니거나 모두일 수도 있습니다. 탈중앙화 되어있기 때문입니다.
- Q: 스마트 미디어 토큰이 안정된 가격에 도달한다면 준비금으로 예치되어 있는 스팀은 영원히 잠기게 됩니까? 이는 좋아 보이지 않습니다. 어떻게 스팀 보유액을 풀어서 스마트 미디어 토큰의 사용자들에게 혜택을 주도록 설정할 수 있습니까?
- A: DRR(감쇠 준비금 비율, decaying reserve ratio) 매개 변수를 설정하면 됩니다. 만약 DRR을 설정한다면, 초과한 만큼의 스팀 준비금을 추가적인 토큰 매입에 활용함으로써 준비금 비율을 미리 정한 값까지 시간에 따라 서서히 감소하도록 만들 수 있습니다. DRR을 설정하는 것은 우수하고 공정하며 탈중앙화된 방법입니다. 이는 후원사가 지출한 것보다 더 많은 투자금을 모아 기대했던 것보다 유망한 ICO를 유치하고, 초과 자본을 기부자들에게 돌려주는 일이기도 합니다. 
- Q: 만약 준비금 비율이 후불 발행 또는 DRR로 인해 시간에 따라 변한다면 이는 고정 준비금 비율이라고 부를 수 없지 않습니까?
- A: 아닙니다. 준비금 비율은 단기적인 관점, 정상적인 조건, 이를 명명한 Bancor의 조건 하에서 일정하기 때문에 고정되었다고 부르고 있습니다. 하지만 이 같은 이름은 다소 오도될 여지가 있습니다.
- Q: 만약 통합 상수가 시간에 따라 변한다면, 이는 상수가 아닌 것이 아닙니까?
- A: 아닙니다. 이는 이를 설명한 계산식에서 수학적인 역할 때문에 통합 상수라고 부르고 있습니다. 미래 버전의 백서에서 다르게 명명될 수도 있을 것입니다.
- Q: 기부금을 DRR로 지정하여 후불 기부하면, 시간이 지남에 따라 감쇠하여 결국 준비금 비율 증가가 무효화 될텐데 왜 이렇게 하겠습니까?
- A: 맞습니다. 이는 기부금의 일부를 즉시 투매하는 것이 허용되지 않는다는 전제하에 시장 조성자에게 효과적으로 기여할 수 있습니다. 시장에 기부금의 상당량을 즉시 투매할 때 나타나는 소동을 피하고 시장 조성자에게 큰 기부를 하고 싶다면 이 방법이 유용할 수 있습니다.
- Q: RR이 감쇠할 때 후불 발행을 위한 DRR을 지정할 수 있습니까?
- A: 그렇습니다.
- Q: 여기서 지정된 시장 조성자는 Bancor 토큰 교환자와 동등합니까?
- A: 그렇지 않습니다. Bancor 토큰 교환자는 합이 100%가 되야하는 다중 준비금 비율을 갖고 있습니다. 또한 토큰 교환자의 형평성을 효과적으로 대표하는 제 3의 토큰을 포함하고 있습니다. 스마트 미디어 토큰의 백서에 등장하는 시장 조성자는 이같은 특징을 갖고 있지 않습니다.
- Q: 사람들이 시장 조성자를 통하지 않고 거래하는 초기 “가격 발견” 기간을 확보하기를 원합니다. ICO로 받은 토큰과 스팀을 시간이 지남에 따라 시장 조성자에게 배분하도록 만들어 0에서 부터 최대 보유액까지 차도록 만들고 싶습니다. 이것이 가능합니까?
- A: 이는 “점진적인 종잣돈”이라 불리며 지원할 계획입니다.
- Q: 수치 안정성이란 무엇입니까?
- A: 시장 조성자는 두 자산의 잔고가 일정한 최소치를 초과할 때만 작동하도록 제한되어 있습니다. 또한 준비금 비율은 일정 범위 내로 제한되며, 모든 메커니즘이 준비금 비율을 증가시키거나 감소시킬 때 특정 범위를 넘어서지 못 하도록 제한될 것입니다. 잠정 수치 실험은 두 자산에 대한 범위를 10,000 사토시 그리고 각각 5%, 50%로 제한할 것을 권고합니다. 이같은 값들은 미래의 실험, 최악 상황 분석, 테스트를 통해 수정될 수 있습니다.
## 스마트 미디어 토큰 운영 비용과 대역폭 비율 제한
---
스팀처럼 스마트 미디어 토큰은 스팀 블록체인 위에서 수수료 없이 전송될 수 있습니다. 스팀은 수수료를 부과하는 대신 계정이 소유한 스팀 비율에 따라 대역폭 비율을 제한합니다. 블록체인은 계정이 일정 기간 동안 전송, 게시 및 다른 작업에 대해 허용되는 대역폭을 결정하기 위해 일시적으로 부여된 계정의 스팀 보유량을 계산합니다. 미래 버전의 스팀에서 [더 나은 유저 인터 페이스를 위해 계정 이름을 소유하면 약간의 대역폭을 허용할 수 있습니다.](https://steemit.com/steemit/@steemitblog/proposing-hardfork-0-20-0-velocity)
### 고품질 사용자 경험을 위해 필요한 무수수료 운영
---
대역폭 비율 제한 덕분에 스팀은 보팅, 게시, 토큰 전송과 같은 기본적인 작업을 수행할 때 애플리케이션과 사용자에게 수수료를 부과하지 않습니다. 스팀 기반의 앱들은 수수료가 없기 때문에 페이스북, 레딧과 같은 ‘좋아요’와 ‘업 보트’ 기능에 수수료를 부과하지 않는 비 블록체인 경쟁사들과 경쟁할 수 있습니다. 만약 이러한 앱들이 수수료를 부과하면 시장에서 받아들여지기 어려울 것입니다.
## 탈중앙화 거래소
---
스마트 미디어 토큰의 중요한 특징 중 하나는 유동 자산 스팀에 대한 무인 시장에 즉각적으로 접근할 수 있다는 것입니다.
### 자동 주문 매칭
---
스팀의 탈중앙화 거래소(DEX) 구조는 매수 호가와 매도 호가가 중첩할 때의 최적의 가격을 자동적으로 매칭시켜줍니다. 다른 DEX들은 중간자를 필요로 하거나 주문을 매칭하기 위한 사용자 에이전트를 필요로 합니다. 중간자를 필요로 하지 않는 자동화된 주문 매칭은 스팀 기반 자산의 보안성, 반복 가능성과 DEX 인터페이스의 안정성을 위해 필요한 중요 기능입니다.
### 다양한 자산 유형들
---
스마트 미디어 토큰 사용자와 생성자가 스팀 DEX를 통해 접근할 수 있는 자산은 스팀, 스팀 달러, 스마트 미디어 토큰, 기본 파생 상품들(IOUs)입니다. 이들 인접 자산은 생성된 모든 스마트 미디어 토큰들의 가시성과 네트워크 효과를 증대시킬 수 있습니다.

스팀은 스팀으로 발행한 자산의 관문 토큰 입니다. 스팀은 스마트 미디어 토큰 전반에 걸친 대역폭 사용량 측정 스틱 역할을 하여 관련성을 유지합니다. 또한 스팀은 모든 스마트 미디어 토큰에 대한 거래 쌍을 이루는 공통 분모 자산 입니다.

스팀 달러(스팀 블록체인 달러, Steem Blockchain Dollars)는 2016년 스팀 출시와 함께 발행되었고, US 달러와 관련된 스팀의 실험적인 자산입니다. 스팀 달러가 US 달러의 IOU 토큰과 경쟁해야 하기 때문에 US 달러 보유자에게 가치를 줄 지는 명확하지 않습니다. 하지만 스팀 달러는 투기꾼에게 가치를 가져다 줄 것입니다.

이 제안에서 서술된 스마트 미디어 토큰은 토큰 생태계를 확장시키기 위해 중요한 역할을 차지하고 있으며, 암호화 자산을 주류 사회에 나오도록 이끌 것입니다. 스마트 미디어 토큰은 DEX를 통해 스팀과 거래 됩니다.

기본 파생상품들(IOUs)은 스마트 미디어 토큰을 통해 발급이 가능합니다. 예를 들어, 만약 스마트 미디어 토큰을 인플레이션 또는 보상 풀 특성을 갖지 않고 발행 한다면, 발행자는 비트코인이나 US 달러 같은 신뢰할 수 있는 현실 자산으로 보증할 수 있을 것입니다. 이 경우 발행자는 비트코인이나 US 달러에 대한 IOU를 거래하여 관문으로서의 비즈니스 기능을 수행할 수 있을 것입니다. 사용자는 스팀 DEX에 대한 접근 권한을 얻기 위해 IOU를 구매할 수 있습니다. 이같은 시장은 다양성과 가치 유동성을 스팀 생태계에 더하는 동시에 DEX의 네트워크 효과를 증진시킬 것입니다.
### 거래 및 전송의 0 수수료
----
스팀 DEX는 스마트 미디어 토큰 생성자와 거래자들을 위한 거래 수수료가 없는 첫 번째 DEX 입니다. 이는 [대역폭 비율 제한](https://github.com/steemit/smt-whitepaper/blob/master/smt-manual/manual.md#--fee--less-operations-necessary-for-quality-user-experience)(스팀 백서와 청서 원본에 서술되어 있음) 때문에 가능합니다. 블록체인이 바이트 단위의 트랜잭션 “가격”을 계산하는 절차에 따라 계정에서 일시적으로 사용할 수 있는 트랜잭션 대역폭을 차감합니다. 이 “가격”은 내부 블록체인 회계로 다른 토큰 잔고에서 인출하지 않습니다.
## 추가적인 기본 컨트랙트로 스마트 미디어 토큰 확장하기
---
스마트 미디어 토큰의 즉각적인 범위에 속하지 않고, 잠재적으로 가치가 있이며 프로그래밍 가능한 컨트랙트가 여럿 있습니다. 하지만 이 컨트랙트 능력은 모듈형으로 생성될 수 있고, 창의적인 기업가와 커뮤니티를 증가시키는 후속 프로젝트는 스마트 미디어 토큰 생태계를 성장 시킬 것입니다.  
### 유급 직책의 커뮤니티 구축
---
스마트 미디어 토큰 커뮤니티는 유급 직책, 협회 역할 또는 프로그래밍 가능한 기본 스마트 컨트랙트로 정의되며 지속적으로 선출된 참가자의 직무로 보강될 수 있습니다. 선출직은 토큰 창업자의 할당량 일부 또는 유급 직책 컨트랙트로 보내지는 기부금을 통해 보상을 받습니다. 유급 직책 컨트랙트는 직책의 연한, 급여의 빈도 및 크기, 지분 가중치를 적용한 선거에 쓰이는 특정 토큰, 참가자가 선출되기 위해 필요한 토큰의 퍼센트, 어떻게 유급 직책 컨트랙트가 사회화되거나 참가자가 선출되지 않을 시 박탈당하는 지를 정의합니다.

유급 역할은 스마트 미디어 토큰을 기반으로 구축된 다양한 애플리케이션, 게임, 비즈니스를 지원하기 위해 활용될 수 있습니다. 유급 직책을 위한 컨트랙트, 직책의 보상 일정, 유급 직책을 선출하기 위해 필요한 보팅 임계값은 누구나 수수료를 지불하면 생성할 수 있습니다. 발행자나 토큰 커뮤니티는 이 직책의 목적을 수립하기 위해 직무 기술과 성과 기대치를 준수 하도록 만드는 헌법을 정할 수 있습니다. 유급 직책의 수는 제한되지 않았고, 유급 직책 컨트랙트는 토큰 창업자의 할당량이나 커뮤니티의 기부금의 일정량을 받을 수 있습니다. 고용될 수 있는 유급 직책의 유형으로는 프론트 엔드 개발자, 전도사, 교육 콘텐츠 제작자, 비즈니스 개발 대표, 그리고 아직 상상하지 못한 수 많은 역할들이 있습니다.
### 화이트 리스트 오라클을 사용하는 민주적인 스마트 미디어 토큰
---
스마트 미디어 토큰은 완전 개방형 접근이 가능한 토큰입니다. 하지만 몇몇 기업은 하나의 허용된 계정만을 사용하게 하거나 게시물 당 1개의 보팅, 일별 X개의 목표 보팅 알고리즘을 도입해 토큰의 잠재력을 높이길 원할 것입니다. 이 알고리즘은 정확한 집단 지성의 콘텐츠 발굴과 토큰 커뮤니티의 민주적인 특성을 위해 쓰일 것입니다. 이를 통합하기 위해 토큰의 보상 풀은 출시할 때만 사용될 수 있는 관리 가능한 화이트 리스트를 가져야 합니다. 화이트 리스트 관리는 토큰을 출시하는 기업이 자체적으로 진행하거나 Civic, Jumio 같은 외부 신원 관리 서비스에 대행해야 합니다. 이 서비스는 스팀 블록체인 위에서 신원 확인이 된 스팀의 사용자 이름으로 피드를 게시하고, 화이트 리스트의 정확성을 보장하기 위해 주기적인 업데이트를 해야합니다. 블록체인 토큰 보상을 지불할 때 토큰을 받는 계정이 화이트 리스트에 속했는지 확인해야 하며, 속하지 않았을 시에 보상 풀로 반환되야 합니다. 
### 연속적인 자금 모금을 위한 2차 ICO
---
벤처 재원을 위해 스마트 미디어 토큰을 활용하는 기업가는 초기 토큰 출시 후에 토큰 경매를 할 수 있는 옵션을 원할 수 있습니다. 기업가는 창업자의 토큰을 출시 당시 비축하고 추후 판매분으로 할당할 수 있습니다. 하지만 이들은 시장에 직접적으로 매도하기보다 토큰 경매 방식을 선호할 수 있습니다.  2차로 경매 형식의 ICO를 지원하기 위한 2차 경매 컨트랙트를 작성할 수 있습니다. 이 컨트랙트는 언제 ICO가 시작되고 얼마나 지속되며, 구매된 토큰에 대한 잠금 기한은 얼마나 되는지 정의해야 할 필요가 있습니다. 이 잠금 기한은 공개 시장에서 할인된 가격으로 판매되도록 만들고, 투자 자본을 유치할 수 있도록 돕습니다. 기업가는 경매 시작전 컨트랙트를 통해 토큰을 전송하며, 토큰은 경매 기간이 끝나는 동시에 경매 참여자들에게 분배됩니다.
### 준비금 유동성 풀에 기반한 스마트 미디어 토큰과의 대역폭 공유
---
스마트 미디어 토큰은 토큰 유동성을 높이고 자동화된 시장 조성자를 생성하기 위해 ICO를 사용합니다. 스마트 미디어 토큰은 시장 조성자의 준비금 풀에 있는 스팀의 양에 비례한 대역폭 권한을 상속받습니다. 스팀에서 모든 “파워 업”되었거나 베스팅 된 스마트 미디어 토큰으로 대역폭의 트랜잭션 권한이 상속됩니다. 스마트 미디어 토큰의 소유자는 기본적으로 스팀 소유량에 관계없이 스마트 미디어 토큰 지분에 비례하여 트랜잭션 대역폭을 할당받습니다. 유동성 풀에 기반한 대역폭 공유은 새로운 토큰이 더 높은 독립성을 갖고 운영될 수 있도록 하며, 스팀에도 비례하는 가치를 기여하게 됩니다.
## 스마트 미디어 토큰이 이더리움같은 일반적인 블록체인 보다 스팀같은 특정 애플리케이션을 위한 블록체인에 더 적합한 이유는 무엇입니까?
---
소프트웨어와 하드웨어 개발 역사를 통해 전문화된 시스템이 일반화된 시스템의 성능을 능가할 가능성이 높다는 사실이 관찰되었습니다. 이와 관련한 예로는 [CPU의 성능을 뛰어넘은 GPU](https://www.quora.com/Whats-the-difference-between-a-CPU-and-a-GPU-When-I-switch-on-my-computer-it-shows-GPU-information-What-does-it-mean), 특정 업무에서 [GPU의 성능을 뛰어넘는 ASIC](https://arstechnica.com/civis/viewtopic.php?t=1203755)이 있습니다. 혹자는 어떻게 스팀 같은 전문화된 블록체인(특정 애플리케이션에 특화된 프로그래밍 기능을 제공하고, 정적 합의 메커니즘을 내장함)이 이더리움 같은 일반 애플리케이션을 위한 블록체인(합의 계층을 넘어 [튜링 완전한](https://en.wikipedia.org/wiki/Turing_completeness) 스마트 컨트랙트 프로그래밍 기능을 제공하고, 새로운 암호화폐 개념을 증명함)보다 스마트 미디어 토큰에 적합한 지 궁금해 합니다. 네트워크 효과나 개발팀 경험을 제외하더라도, 스팀의 장점은 컴퓨터 과학, 소비자 안전, 경제적인 관점에서 드러납니다.
### 스마트 미디어 토큰은 특정 애플리케이션에 특화된 블록체인 환경에서 안전하고 비용 효율적입니다.
---
스팀처럼 고유하고, 특화된 프로그래밍 환경에서 스마트 미디어 토큰은 코드 안정성과 신뢰성에 근거한 효율성으로부터 가치를 얻습니다. 반면 이더리움과 테조스 처럼 일반적인 애플리케이션을 위한 플랫폼에서는 새로운 토큰과 발행자에 대해 비싸고 가정에 기반한 회계감사를 거쳐야만 안정성이 확보될 수 있습니다. 이러한 일반적인 애플리케이션을 위한 프로토콜 중 일부는 중요한 [정식 검증](https://en.wikipedia.org/wiki/Formal_verification)을 요구합니다. 하지만 감사 비용의 대부분은 발행자의 토큰 메커니즘 선택, 클라이언트의 코드 작성을 하기 위한 선택, 토큰의 사용자 정의 코드가 차지합니다. 목적성있는 코드 설계와 스팀을 통해 스마트 미디어 토큰은 토큰 출시 후 토큰 보유자들에게 잠재적인 해를 끼치지 않으면서 조정이 가능한 정적(vs 동적) 암호경제학적인 특성을 지원할 수 있습니다. 정적 또는 동적 경제학 특성간의 의도적인 기술은 토큰의 안정성 감사를 간단하고 저렴하게 수행할 수 있도록 만들어 줍니다.

이 문제를 설명하기 위해 누군가 그들의 화폐 중 20%를 미화 $100과 교환하자는 조건을 제안했다고 가정해봅시다. 그렇다면 당신은 판매자에게  “판매자가 통화를 더 발행할 권리를 이용하여 화폐 가치를 희석할 수 있습니까?”와 같은 거래의 3차 현실을 조사하는 필수적인 질문을 던질 수 있습니다. 스마트 미디어 토큰 보유자는 출시 후 변할 수 없는 발행이나 인플레이션 비율과 같은 정적 특성을 갖는 스마트 미디어 토큰의 핵심 경제에 의존할 수 있습니다. 그러므로 소비자는 예상치 못한 화폐 발행으로 인한 피해를 피할 수 있습니다. 이더리움과 테조스 같은 일반적인 애플리케이션을 위한 공개 프로그래밍 블록체인 프로토콜에서는 소비자 안전을 보호하는 플랫폼 기반의 설계 원리와 신뢰성이 없습니다. 
### 스팀의 스마트 미디어 토큰은 창작 증명의 인센티브를 핵심 토큰과 조정합니다.
---
스팀과 달리 창작 증명의 콘텐츠 보상을 줄 수 없는 핵심 토큰들(이더리움 등)은 수익, 중요 활동 사용자층, 공유 영향력 및 부트스트래핑 혜택을 새로운 스마트 미디어 토큰 커뮤니티에 제공하지 못합니다. 반면 스팀은 보상 풀 특징과 중요 사용자층을 새로운 네트워크에 빌려주고, 부트스트랩과 판로를 도와 네트워크 참여자의 성공적인 독립 클러스터가 될 수 있도록 만들어 줍니다. 반대로 일부 기업가는 스팀으로부터 독립적인 스마트 미디어 토큰을 채택하는 전략을 검토하고 결정할 것입니다. 또한 이더리움의 ERC20 처럼, 스마트 미디어 토큰은 스팀만 배경으로 실행하면서 트랜잭션 비용을 위해 필요한 대역폭만 계산할 수 도 있습니다.
### 스팀의 스마트 미디어 토큰은 양질의 사용자 경험을 위한 트랜잭션 비용이 있습니다
---
대역폭의 비율을 제한하여 운영 하든 노골적인 수수료를 부과 하든 일반 목적의 블록체인은 애플리케이션의 조그만 부분 이상에 대해 효과적으로 트랜잭션 가격을 매길 수 없습니다. 이더리움 같은 일반적인 애플리케이션용 블록체인 위에서 스마트 미디어 토큰은 사용자 경험을 저하시키는 결과를 초래할 것입니다. 이와 관련한 명백한 예시로 이더리움 같은 블록체인은 모든 트랜잭션에 대해 노골적인 수수료를 부과합니다. 하지만 어떠한 콘텐츠 게시자도 사용자가 댓글을 남기거나 게시물에 좋아요를 남기는데에 수수료를 부과하기를 원하지 않을 것입니다. 이더리움 위에서 스마트 미디어 토큰을 사용하면 이같은 수수료가 필수적이기 때문에, 이더리움은 스마트 미디어 토큰의 플랫폼으로 적합하지 않습니다.

이더리움과 달리, 일부 미래 개방형 프로그래밍 가능한 블록체인은 트랜잭션 수수료로 대역폭 비율 제한을 사용합니다. 하지만 대역폭 비율 제한은 특정 애플리케이션의 사용자 경험 요구사항을 만족시키기 위해 미세한 조정을 필요로 합니다. 예를 들어, 스팀에서 대역폭 비율 제한은 콘텐츠 애플리케이션과 그들의 사용자 상호작용을 지원하기 위해 조정됩니다. 두 가지 객체(소유 토큰의 수량, 계정 소유권)에 따라 대역폭 권한을 활용할 수 있습니다. 각각에 대한 최적의 대역폭 허용치를 개선하기 위해 1년 간의 생산 수준의 연구를 진행하였습니다. 일반적으로 개방형 프로그래밍 가능한 플랫폼의 경우, 정확한 가격 책정에 대한 부담과 요구는 애플리케이션이 사용자 행동에 적절하게 가격을 책정할 지 못하도록 방해할 수 있습니다. 이 문제는 블록체인의 자원을 늘리고 공유하는 수많은 잠재적인 애플리케이션 테스트를 만들어내어 상황을 악화시킬 수 있습니다. 따라서 고유의 특정 애플리케이션을 지원하는 블록체인은 사용자 경험을 이와 관련된 토큰과 연결시키기 때문에 더 적합한 트랜잭션 가격을 책정할 수 있습니다.
### 전문화된 애플리케이션의 집합으로 스케일링된 프로그램 절차를 가지는 블록체인의 수혜를 받는 스마트 미디어 토큰
---
블록체인 스케일링은 블록체인이 여러 명령을 어떻게 한 번에 처리하게 확장할 수 있는가에 대한 내용이며, 이와 관련한 최첨단 개념으로   “샤딩”(Vitalik Buterin과 이더리움 프로젝트로부터 기원)과 “다중 스레드 병렬 처리”(스팀의 Michael Vandeberg로부터 기원)가 있습니다. 이더리움 같은 일반 목적용 플랫폼은 스케일링에 다가서기 위한 좋은 시험대 입니다. 하지만 이더리움이 발견한 모든 제품 시장의 적합성을 갖는 플랫폼을 스팀처럼 반복적인 개선을 하는 더욱 전문화된 모델에 적용하면, 제품 시장 적합도에 따라 발견된 요구를 만족하는 효과적인 절차로 스케일할 수 있습니다.

1990년대와 2000년대 초반을 돌이켜보면, 컴퓨터 과학계가 GPU에 최적화된 코드를 작성하기 시작할 때 더 큰 스케일링을 위해 FPGA(필드 프로그래머블 게이트 어웨이)가 등장했습니다. FPGA는 어떤 상상할 수 있는 회로의 형태로 논리 게이트 집합을 프로그래밍 할 수 있게 도와주는 주는 칩 입니다.  FPGA는 효과적으로 ASIC(높은 전력을 소모 함) 프로토타입을 설계할 수 있습니다. FPGA의 단위 와트당 성능은 ASIC과 같지 않지만, 특정 업무에 대한 처리 속도는 CPU보다 빠릅니다. 이러한 플랫폼들은 한 컨트랙트에서 다른 컨트랙트를 호출하는 것을 비롯해 점점 더 일반화되고 있습니다. 다른 컨트랙트를 호출하는 것은 다중 병렬 처리 프로세스를 단일 코어  프로세스의 성능으로 줄이기 때문에 최적화된 스케일에서 멀어지도록 만들 수 있습니다. CPU가 GPU 보다 최적화 될 수 없는 것처럼 이더리움, 게오스, 테조스 같은 플랫폼은 스팀 같은 튜닝 불완전한 전문화 애플리케이션 블록체인 보다 최적화 될 수 없습니다. CPU 같은 블록체인은 예상치 못한 프로세싱 요구사항으로 인해 병목현상이 발생할 수 있지만, 스팀 같은 궁극의 블록체인 플랫폼은 특별 설계가 가능합니다. 또한 FPGA가 병렬 처리 알고리즘을 이용해 스케일링을 한 것과 같이 최적화를 할 수 있을 것입니다.
### 콘텐츠 관리 시스템 [(CMS)](https://en.wikipedia.org/wiki/Content_management_system) 기초 요소를 갖춘 블록체인의 수혜를 받는 스마트 미디어 토큰
---
이더리움과 같은 일반 애플리케이션을 위한 블록체인(핵심 프로토콜에서 특정 애플리케이션만을 위한 기초 요소를 갖는 것을 본질적으로 피함)과 달리, 스팀은 평문과 일반 구조 데이터를 동시에 저장하기 위한 구조화된 공공 콘텐츠 데이터 베이스를 제공합니다. 개발자는 계정 이름, 게시글, 댓글, 보팅, 계정 잔고 등의 콘텐츠 기초 요소를 만들 수 있습니다. 이 기초 요소는 블록체인 기반의 애플리케이션이 애플리케이션 상호 운용성을 구축하고 개발자가 빠르게 적응할 수 있도록 도와주는 역할을 합니다. 이러한 기초 요소가 없으면 블록체인 기반 애플리케이션마다 2차 데이터베이스가 구축될 필요가 생기고, 2차 애플리캐이션 별로 특화된 데이터베이스간의 경쟁을 부축일 것입니다. 여러 2차 콘텐츠 데이터베이스 층들은 콘텐츠 관리 시스템(CMS)으로서 블록체인이 갖는 잠재적인 네트워크 효과를 분산시킵니다. 또한 최종 사용자들이 한 블록체인 기반 애플리케이션에서 다른 블록체인 기반 애플리케이션으로 유동적으로 움직일 수 없게 만들어 소비자의 안전 혜택을 줄이며, 잠재적인 애플리케이션의 상호 운용성을 감소시킵니다.
## 스팀과 스마트 미디어 토큰에 대한 증가하는 시장 수요 및 수수료보다 매력적인 내재적 가치 창출요소들
---
스팀과 스마트 미디어 토큰 생성을 통한 여러가지 가치 창출 요소들이 있습니다.
### 트랜잭션 대역폭 확보를 위해 구입한 스팀으로 참여한 스마트 미디어 토큰을 통해 최대 수익을 얻을 수 있습니다
---
스마트 미디어 토큰의 등장에 따라, 사용자들이 스팀을 보유하고자 하는 수요가 증가할 것입니다. 사용자는 각 스마트 미디어 생태계 속에서 커가는 잠재력에 상응하는 속도로 발전하는 스팀 서비스에 참여하고, 소비하고, 이용하고자 하기 때문에 스팀을 더 많이 보유하게 될 것입니다. 간단히 말하자면 고급 사용자가 스마트 미디어 토큰 커뮤니티 내에서 잠재적인 소득을 높이려고 할 때 최고의 수익률을 얻기 위해서는 대역폭 허용치를 확보하기 위해 더 많은 스팀을 필요로 하게 됩니다. 애플리케이션 수준에서 대역폭에 대한 수요는 초과 대역폭을 위임할 수 있는 사용자나 비즈니스에 의해 충족될 것입니다.
### 자동화된 시장 조성자에 의해 유동성 풀로 잠기는 스팀 공급
---
자동화된 시장 조성자가 활용하는 각 스마트 미디어 토큰은 스팀에 대한 수요 비율을 공급 가능한 스팀의 비율로 증가시킵니다. 스팀에 자동화된 시장 조성자가 끼치는 영향은 각 자동화된 시장 조성자가 사용가능한 공급량을 감소시키는 영원한 스팀 풀을 보유를 한다는 것입니다. 수요가 일정하다면, 새로운 자동화된 시장 조성자의 등장으로 스팀의 가격은 상승하게 될 것입니다.
### 새로운 영향력의 등장에 따른 스팀과 스마트 미디어 토큰 수요 증가
---
잠재적인 유용성 관점에서 스팀에 대한 수요는 스마트 미디어 토큰 보상 풀에 대한 스팀 파워의 영향력 공유와 생성되는 스마트 미디어 토큰에 의해 증가하게 됩니다. 스마트 미디어 토큰 보상 풀에 대한 스팀 파워 기반 공유 영향력을 추적함에 따라, 스팀에 대한 수요를 증가시키는 새로운 권리와 사용법을 제공할 수 있습니다. 이 권리는 스마트 미디어 토큰에서 스마트 미디어 토큰으로 증여가 가능하며, 가치의 흐름은 동일한 양식을 띠게 됩니다.
### 스마트 미디어 토큰 ICO 증가에 따른 스팀의 수요 증가
---
플랫폼 차원에서 수요를 유발할 수 있는 다른 원인으로는 새로운 자본을 생태계로 끌어 들일 수 있는 ICO 같은 독점적인 자금 조달 기회가 포함될 수 있습니다. 처음에 기본 자산인 스팀으로 유입되며 이후 스마트 미디어 토큰으로 유입되게 됩니다. ICO로 인해 생태계에 증가한 자본은 보유한 스팀에 대한 순자산 증식에 대한 기회를 줍니다. 최악의 경우 토큰을 제공한 기관이 스팀을 모두 팔아서 기본 자산의 가치가 사라질 수 도 있습니다. 최악의 상황에 대한 예는 ICO가 시작하고 나서 스마트 미디어 토큰을 구입하기 위해 $100로 스팀을 산 후, ICO에 의해 모은 스팀의 100%를 US 달러로 모두 팔아버리는 것입니다. 이렇게되면 스팀의 가치와 관련된 명백한 순효과가 하나도 없습니다. 하지만 스팀 가치에 대한 ICO의 순효과 기여도가 겉보기에 0라도, 새로운 관심 또한 가치라고 한다면 스팀과 스팀 생태계가 받게 되는  관심으로 인한 내재적인 순이익이 있을 수 있습니다. 더욱이, 이더리움의 ICO 행위에 기반하여 ICO 기관이 모금한 스팀의 대부분을 투기 혹은 약속에 기초하여 계속 보유하고 보유 가치를 창출할 것이라 기대하는 것이 합리적입니다. 
### 스팀: 세계적인 광고 네트워크
---
이런 새로운 가치 창출 메커니즘과 함께 스팀을 위해 생성된 고유 가치를 인식하는 것이 필수적입니다. 암시적인 관심과 광고 네트워크의 가치를 창작 증명 보상을 이용하는 모든 스마트 미디어 토큰에 적용할 수 있습니다. 스팀 같은 스마트 미디어 토큰은 내재된 광고 네트워크로서 신뢰성과 자격 증명을 제공하는 보상 풀과 같은 고유의 큐레이션 특성을 가지고 있습니다. 스마트 미디어 토큰의 보상 풀은 steemit.com 처럼 완전히 스마트 미디어 토큰과 통합된 인터페이스를 바랍니다. 이 서비스에서는 보류중인 게시물에 대한 스마트 미디어 토큰 지불금을 존중하며, 보류 지불금이 높은 게시물부터 낮은 것까지 순서대로 나열합니다(“트랜딩”이라고 부름). 트랜딩 페이지는 스마트 미디어 토큰 보유자 커뮤니티에 의해 감사를 받습니다. 다른 스마트 미디어 토큰과 마찬가지로 스팀에 동등하게 적용되는 이 효과는 정렬된 “트랜딩” 페이지 입니다. 사용자들(블로거, 비디오 블로거, 광고주)은 이목을 끌기 위해 페이지의 상단을 구매할 때 “트랜딩” 페이지를 이용해 잠재적인 수익을 안정적으로 평가할 수 있습니다. 이 참여자들은 **콘텐츠를 홍보하기 위해 스팀과 스마트 미디어 토큰을 구매하거나 임대**하는 결정을 하게됩니다. 이 과정을 통해 광고주가 노출 효과를 얻기 위해 스팀/스마트 미디어 토큰을 구매하거나 임대하는 결정을 할 때 스팀/스마트 미디어 토큰의 수요가 높아지게 됩니다. 이같은 가치 주도적인 특성은 “이더리움: 세계의 컴퓨터”로 기술된 것과 비슷하지만 다르게 “스팀: 세계의 광고 네트워크”로 표현할 수 있습니다.
## 스마트 미디어 토큰 지원을 위한 스팀 생태계
---
### 웹사이트와 앱에 스마트 미디어 토큰을 통합하기
---
#### API와 문서
스마트 미디어 토큰을 위해 지속적으로 업데이트될 예정 입니다. 현재 스팀 APIs는 아래 주소에 존재합니다: http://steem.readthedocs.io/en/latest/index.html 과 https://steemit.github.io/steemit-docs/
#### 계정 생성, 키 서명, 지갑 기능을 위한 공유 도구들
몇몇 공유 도구는 가입, 트랜잭션 서명, 스마트 컨트랙트 같은 지갑 기능을 위탁하길 바라는 애플리케이션을 지원하기 위해 존재합니다. [SteemConnect](https://v2.steemconnect.com/)는 스마트 미디어 토큰을 지원하는 동시에 암호화폐에 대한 경험이 적은 기업가가 개발하는 애플리케이션 또한 지원합니다. 
## 결론
---
개방형 자산 발행, 트랜잭션 비용 같은 대역폭 비율 제한, 영원히 사용가능한 콘텐츠, 실시간 트랜잭션 속도, 토큰의 자율적인 배분, 탈중앙화 거래소, 자동화된 시장 형성 및 ICO 컨트랙트를 위한 특수 설계의 조합을 통해 스팀은 인터넷 게시자를 위한 최고의 토큰 프로토콜을 제공합니다.
## 참고 문헌
---
[1] Steemit, Inc., 2017. Steem Bluepaper. A protocol for bringing smart, social currency to publishers and content businesses across the internet. (https://www.steem.io/steem-bluepaper.pdf)

[2] Eyal Hertzog, Guy Benartzi & Galia Benartzi, 2017. Bancor Protocol. Continuous Liquidity and Asynchronous Price Discovery for Tokens through their Smart Contracts. (https://www.bancor.network/static/bancor_protocol_whitepaper_en.pdf)
## 부록
---
### 구현 노트
---
다음은 스마트 미디어 토큰 출시 일정에 대한 타임 라인 및 상태 다이어그램입니다.
![fig10](https://github.com/steemit/smt-whitepaper/blob/master/smt-manual/img/timeline.png)
그림 10: 스마트 미디어 토큰 출시에 대한 타임 라인
#### 스마트 미디어 토큰 명명 표준
- 스마트 미디어 토큰의 이름은 3-10개의 대문자 ASCII 문자를 사용해야 합니다(A-Z).
- 스마트 미디어 토큰의 이름은 `STEEM`, `SBD` 또는 `VESTS`와 같아서는 안됩니다.
#### 자산 디렉토리 표준
***디렉토리*** 는 각각의 NAI중 하나의 상태와 연결되야 합니다.
~~~
Listed (목록에 오름)
Deprecated (반대 됨)
Unlisted (목록에서 삭제)
Blacklisted (블랙 리스트에 오름)
~~~
각각의 가능한 자산 이름은 다음 중 한 가지 상태와 연결되야 합니다.
~~~
Free (자유)
Reserved (예약)
~~~
`Listed`나 `Deprecated` NAI는 관련된 이름을 가지고 있어서 연결할 때 `Reserved`의 목록으로 들어가야 합니다.
사용자 인터페이스는 다중 자산 디렉토리를 단일 자산 디렉토리로 결합하여 디렉토리를 증가시키는 ***자산 디렉토리 결합*** 기능을 제공합니다. 자산 디렉토리 결합은 NAI가 다른 디렉토리에 다르게 나열되어 있는 문제를 해결하기 위해 다음과 같은 알고리즘을 이용합니다. 
- (1) 만약 NAI가 어떤 구성 요소 디렉토리에서 `Blacklisted` 되어 있다면 `Blacklisted`를 반환합니다.
- (2) 만약 NAI가 다중 구성 요소 디렉토리에서 `Listed` 또는 `Deprecated` 되어 있다면 모든 구성 요소 디렉토리는 관련된 이름에 동의하지 않고 `Unlisted`를 반환합니다.
- (3) 만약 NAI가 적어도 하나의 구성 요소 디렉토리에서 `Listed` 되어 있다면 `Listed`를 반환합니다.
- (4) 만약 NAI가 적어도 하나의 구성 요소 디렉토리에서 `Deprecated` 되어 있다면 `Deprecated`를 반환합니다.
- (5) `Unlisted`를 반환합니다.

이와 마찬가지로,  다른 디렉토리에 다르게 나열된 이름을 해결하는 방법은 다음과 같습니다.
- (1) 만약 이름이 어떤 구성 요소 디렉토리에서 `Reserved` 되어 있다면, `Reserved`를 반환합니다.
- (2) `Free`를 반환합니다.

동적인 디렉토리(URL 또는 블록체인 계정에 기반을 둠)는 5분 이상 캐시되지 않아야 합니다.
#### 스마트 미디어 토큰 이름을 위한 사용자 인터페이스 가이드라인
- 사용자 인터페이스는 기본 자산 디렉토리를 가질 수도 있지만 꼭 필요한 것은 아닙니다.
- 사용자 인터페이스는 목록에 없는 NAI를 숨길 수 있습니다.
- 사용자 인터페이스는 사용자가 사용자 인터페이스 기본 사항을 그들 소유의 자산 디렉토리에 덮어 쓰거나 보강하는 것을 허용합니다.
- 사용자 인터페이스는 사용자가 활발하게 트랜잭션하고 있지만 목록에 없는 NAI를 숨길 때 재고해봐야 합니다.
#### 자산 디렉토리를 위한 운영 가이드라인
- 자산 디렉토리는 다른 이름을 참조하기 위해 잘 알려진 NAI를 설정하거나 다른 NAI를 참조하기 위해 잘 알려진 이름을 설정하여 사용자가 혼동을 겪게 하면 안됩니다.
- 자산 디렉토리는 자산을 디렉토리에 추가하려고 하는 스마트 미디어 토큰 생성자와 사용자 인터페이스에 디렉토리를 추가하려고 하는 사용자 인터페이스 개발자 모두에게 목록을 표시하는 과정을 명확하게 만들어 주어야 합니다.
#### 자산 디렉토리 형식
URL과 파일 기반 자산의 디렉토리는 JSON 형식으로 되어 있습니다. 세부 사항은 구현과 동시에 개발될 것입니다. 블록체인 기반 디렉토리는 사용자 정의 JSON 작업을 사용할 것입니다. 다시, 세부 사항은 구현과 동시에 개발될 것입니다.
### 단위 테스트
---
단위 테스트에 대한 세부 사항은 구현과 동시에 개발될 것입니다. 
