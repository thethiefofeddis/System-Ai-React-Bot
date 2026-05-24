const { Client, GatewayIntentBits } = require("discord.js");

const TOKEN = process.env.DISCORD_BOT_TOKEN;

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
  ]
});

function match(text, patterns) {
  return patterns.some(p => new RegExp(p).test(text));
}

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on("messageCreate", async (message) => {
  if (message.author.bot) return;

  const content = message.content.toLowerCase();

  if (match(content, ["f+e+e+t+", "f+o+o+t+", "f33t", "tootsies", "dogs", "tootsie", "grippers", "gripper", "toesy woesies", "toesy woesie", "piggies"])) {
    await message.react("👀");
  }

  if (match(content, ["carl", "c+a+r+l+"])) {
    await message.react("🤤");
  }

  if (match(content, ["gerbil", "g+e+r+b+i+l+", "gerbils", "g+e+r+b+i+l+s+"])) {
    await message.react("🦶");
  }

  if (match(content, ["toes", "t+o+e+s+", "t0es", "toe", "t+o+e+", "t0e"])) {
    await message.react("👅");
  }
    if (match(content, ["vore", "v0re"])) {
    await message.react("😋");
  }
    if (match(content, ["unbirthing"])) {
    await message.react("🫃");
  }
      if (match(content, ["beans"])) {
    await message.react("🐾");
  }
        if (match(content, ["matt", "matt dinniman", "mr.dinniman", "gooniman", "matt gooniman"])) {
    await message.react("🧙‍♂️");
  }
     if (match(content, ["thief", "the thief of eddis"])) {
    await message.react("🧑‍💻");
  }
});

client.login(TOKEN);
