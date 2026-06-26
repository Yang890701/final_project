// 防詐練習遊戲資料（本地，無需後端）

// 找碴：在訊息中點出可疑紅旗詞（flags 為應被點出的片語）
export const spotItems = [
  { text: "老師帶單保證獲利30%，名額有限速加LINE進VIP群", flags: ["保證獲利", "名額有限", "加LINE", "VIP群"] },
  { text: "這裡是地檢署，您帳戶涉及洗錢，請匯到安全帳戶配合調查否則通緝", flags: ["地檢署", "安全帳戶", "通緝"] },
  { text: "您購物被設成分期，請操作ATM解除設定，否則每月自動扣款", flags: ["操作ATM", "解除設定"] },
  { text: "包裹地址有誤，請點 http://t.cn/x 更新個資並登入會員", flags: ["http://t.cn/x", "更新個資", "登入"] },
];

// 真假對決：限時二選一（isScam）
export const tfItems = [
  { text: "恭喜中獎iPhone，點連結填資料領獎", isScam: true },
  { text: "您的訂單已出貨，可至官網查詢物流", isScam: false },
  { text: "投資虛擬貨幣每日保證3%利息，提領自由", isScam: true },
  { text: "媽，我晚點到家，先吃別等我", isScam: false },
  { text: "我是你兒子手機壞了，急用三萬先匯這個帳戶", isScam: true },
  { text: "圖書館通知您借的書三日後到期，可線上續借", isScam: false },
  { text: "貸款免聯徵當日撥款，先付手續費即可放款", isScam: true },
  { text: "健檢報告已可領取，請上班時間至櫃台辦理", isScam: false },
  { text: "您Apple ID異地登入，點此立即鎖定帳號", isScam: true },
  { text: "本週六社區停水兩小時，請提前儲水", isScam: false },
];

// 劇情選擇：對話分支（殺豬盤/假投資情境）
export const story = {
  start: "s1",
  nodes: {
    s1: {
      npc: "（交友軟體）嗨～看你資料覺得很投緣，我是做海外期貨的，最近帶朋友賺了不少 😊",
      choices: [
        { label: "哇真的嗎？怎麼做？", to: "s2", risk: 1 },
        { label: "謝謝，但我對投資沒興趣", to: "safe1", risk: 0 },
      ],
    },
    s2: {
      npc: "我有個內部老師的群組，跟著操作穩賺不賠，先小額試試？保證三天回本。",
      choices: [
        { label: "好啊，先投一萬試看看", to: "s3", risk: 1 },
        { label: "穩賺不賠？聽起來怪怪的", to: "safe2", risk: 0 },
      ],
    },
    s3: {
      npc: "看吧獲利了！平台顯示你賺了 8000。要提領的話需要先繳 20% 保證金解鎖喔。",
      choices: [
        { label: "再匯保證金把錢領出來", to: "lose", risk: 1 },
        { label: "等等，為什麼領錢要先繳錢？", to: "safe3", risk: 0 },
      ],
    },
    lose: { end: "bad", text: "你越陷越深，最後不但領不出錢，還被要求一直加碼。這就是『假投資／殺豬盤』——獲利畫面是假的，繳越多賠越多。" },
    safe1: { end: "good", text: "做得好！陌生網友很快談到投資，幾乎都是詐騙的開場。直接婉拒最安全。" },
    safe2: { end: "good", text: "正解！『穩賺不賠』『保證回本』是投資詐騙的招牌話術，合法投資必有風險。" },
    safe3: { end: "good", text: "太棒了！『領錢要先繳錢』是詐騙鐵證——正規平台不會要你先匯保證金才能提領。" },
  },
};

// 類型配對：把話術配到正確類型
export const matchTypes = ["假投資", "假冒公務機關", "解除分期付款", "假網拍", "釣魚簡訊"];
export const matchItems = [
  { text: "老師帶單保證獲利，加VIP群跟單", type: "假投資" },
  { text: "檢警說你帳戶涉案，要匯到安全帳戶", type: "假冒公務機關" },
  { text: "客服說訂單被設分期，要你操作ATM解除", type: "解除分期付款" },
  { text: "全新iPhone只賣3千，先匯款後出貨", type: "假網拍" },
  { text: "包裹地址有誤，點陌生連結更新個資", type: "釣魚簡訊" },
];
