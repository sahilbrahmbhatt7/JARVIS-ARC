$(document).ready(function () {


    $('.text').textillate({

        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });

    //wave
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.1",
        autostart: true
    });

    //siri message animation

    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },
    });

    //mic click event

    $("#MicBtn").click(function () {

        micClickedUI();
    });

    function micClickedUI() {
        eel.playAssistantSoundY();

        $("#Ovel").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        $("#Settings").attr("hidden", true);
        $("#sclose").attr("hidden", true);

        eel.engine_loop();
    }

    function doc_keyUpClap(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'o' && e.metaKey) {
            micClickedUI();
        }
    }
    document.addEventListener('keyup', doc_keyUpClap, false);

    //stopBtn
    $("#StopBtn").click(function () {

        eel.playAssistantSound()

        $("#Ovel").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
        $("#Settings").attr("hidden", true);
        $("#sclose").attr("hidden", true);

        eel.stop_s()
    });
    //JARVIS KEYWORD
    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'j' && e.metaKey) {
            micClickedUI();
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    function PlayAssistant(message) {

        if (message != "") {

            $("#Ovel").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            $("#Settings").attr("hidden", true);
            $("#sclose").attr("hidden", true);
            eel.engine_loop(message);
            $("#chatbox").val("")
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);

        }

    }

    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)

    });

    // send button event handler
    $("#SendBtn").click(function () {

        let message = $("#chatbox").val()
        eel.set_status(1)  // Set status to 1 to indicate message is being processed
        PlayAssistant(message)

    });

    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            eel.set_status(1)  // Set status to 1 to indicate message is being processed
            PlayAssistant(message)
        }
    });

    $("#SettingsBtn").click(function () {

        $("#Ovel").attr("hidden", true);
        $("#SiriWave").attr("hidden", true);
        $("#Settings").attr("hidden", false);
        $("#sclose").attr("hidden", false);
    });

    $("#sclose").click(function () {

        $("#Ovel").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
        $("#Settings").attr("hidden", true);
        $("#sclose").attr("hidden", true);
    });

    $("#addData").click(function () {

        let key = $("#key").val()
        let path = $("#path").val()

        database(key, path)
    });

    function database(key, path) {
        eel.engine_loop(path)
        if (key != "") {
            if (path != "") {
                eel.add(key, path)

            }
            eel.engine_loop(path)
            eel.add(key, path)
        }

    }
// ==================== Counters ====================
let systemCount = 0;
let webCount = 0;
let videoCount = 0;
let contactCount = 0;


// ==================== Load Commands from DB ====================
function loadSettings() {

    // Reset counts
    systemCount = 0;
    webCount = 0;
    videoCount = 0;
    contactCount = 0;

    // Clear tables
    $("#systemSettingsTable").empty();
    $("#webSettingsTable").empty();
    $("#videoSettingsTable").empty();
    $("#contactSettingsTable").empty();


    // Load System
    eel.getSys()(function (data) {
        data.forEach(item => addRow("system", item[0], item[1]));
    });

    // Load Web
    eel.getWeb()(function (data) {
        data.forEach(item => addRow("web", item[0], item[1]));
    });

    // Load Video
    eel.getVideo()(function (data) {
        data.forEach(item => addRow("video", item[0], item[1]));
    });

    // Load Contacts
    eel.getContacts()(function (data) {
        data.forEach(item => addContactRow(item[0], item[1]));
    });
}


// ==================== Helper: Truncate ====================
function truncateString(str, maxLength = 40) {
    if (!str) return "";
    return str.length > maxLength ? str.substring(0, maxLength) + "..." : str;
}


// ==================== Add Row (System/Web/Video) ====================
function addRow(type, key, path) {

    let count, tableId;

    if (type === "system") {
        systemCount++;
        count = systemCount;
        tableId = "#systemSettingsTable";
    } else if (type === "web") {
        webCount++;
        count = webCount;
        tableId = "#webSettingsTable";
    } else if (type === "video") {
        videoCount++;
        count = videoCount;
        tableId = "#videoSettingsTable";
    }

    const displayKey = truncateString(key, 20);
    const displayPath = truncateString(path, 40);

    const row = $(`
        <tr>
            <td>${count}</td>
            <td class="key" title="${key}">${displayKey}</td>
            <td title="${path}">${displayPath}</td>
            <td>
                <button class="btn btn-danger btn-sm delete-btn" data-type="${type}">
                    <i class="bi bi-trash"></i>
                </button>
            </td>
        </tr>
    `);

    $(tableId).append(row);
}


// ==================== Add Contact Row ====================
function addContactRow(name, number) {

    contactCount++;

    const displayName = truncateString(name, 20);

    const row = $(`
        <tr>
            <td>${contactCount}</td>
            <td class="contact-name" title="${name}">${displayName}</td>
            <td>${number}</td>
            <td>
                <button class="btn btn-danger btn-sm delete-contact-btn">
                    <i class="bi bi-trash"></i>
                </button>
            </td>
        </tr>
    `);

    $("#contactSettingsTable").append(row);
}


// ==================== Add Commands ====================

// System
$("#addSysData").click(function () {
    const key = $("#sys-key").val().trim();
    const path = $("#sys-path").val().trim();
    if (!key || !path) return;

    eel.addSys(key, path);
    addRow("system", key, path);

    $("#sys-key").val("");
    $("#sys-path").val("");
});

// Web
$("#addWebData").click(function () {
    const key = $("#web-key").val().trim();
    const url = $("#web-url").val().trim();
    if (!key || !url) return;

    eel.addWeb(key, url);
    addRow("web", key, url);

    $("#web-key").val("");
    $("#web-url").val("");
});

// Video
$("#addVideoData").click(function () {
    const key = $("#video-key").val().trim();
    const path = $("#video-path").val().trim();
    if (!key || !path) return;

    eel.addVideo(key, path);
    addRow("video", key, path);

    $("#video-key").val("");
    $("#video-path").val("");
});


// ==================== Add Contact ====================
$("#addContactData").click(function () {

    const name = $("#contact-name").val().trim();
    const number = $("#contact-number").val().trim();

    if (!name || !number || number.length !== 10 || !/^\d+$/.test(number)) {
        alert("Enter valid 10 digit number");
        return;
    }

    const fullNumber = "+91" + number;

    eel.addContact(name, fullNumber);
    addContactRow(name, fullNumber);

    $("#contact-name").val("");
    $("#contact-number").val("");
});


// ==================== CSV Upload ====================
$("#uploadCsvBtn").click(function () {

    const file = document.getElementById("contactCsvUpload").files[0];
    if (!file) return alert("Select CSV file");
    

    const reader = new FileReader();

    reader.onload = function (e) {
        eel.importContactsCSV(e.target.result);  // send full CSV text to Python
        //CLEAR TABLE
            $("#contactSettingsTable").empty();
            contactCount = 0;

            //RELOAD FROM DATABASE
            eel.getContacts()(function (data) {
                data.forEach(item => {
                    addContactRow(item[0], item[1]);
                });
            });
    };

    reader.readAsText(file);
});


// ==================== Delete Commands ====================
$(document).on("click", ".delete-btn", function () {

    const row = $(this).closest("tr");
    const key = row.find(".key").attr("title"); // use full key
    const type = $(this).data("type");

    if (type === "system") {
        eel.deleteSys(key);
        row.remove();
        renumberRows("system");

    } else if (type === "web") {
        eel.deleteWeb(key);
        row.remove();
        renumberRows("web");

    } else if (type === "video") {
        eel.deleteVideo(key);
        row.remove();
        renumberRows("video");
    }
});


// ==================== Delete Contact ====================
$(document).on("click", ".delete-contact-btn", function () {

    const row = $(this).closest("tr");
    const name = row.find(".contact-name").attr("title");

    eel.deleteContact(name);
    row.remove();
    renumberContactRows();
});


// ==================== Renumber ====================
function renumberRows(type) {

    let tableId;

    if (type === "system") tableId = "#systemSettingsTable";
    if (type === "web") tableId = "#webSettingsTable";
    if (type === "video") tableId = "#videoSettingsTable";

    let count = 0;

    $(tableId + " tr").each(function () {
        count++;
        $(this).find("td:first").text(count);
    });
}

function renumberContactRows() {

    contactCount = 0;

    $("#contactSettingsTable tr").each(function () {
        contactCount++;
        $(this).find("td:first").text(contactCount);
    });
}


// ==================== Open Settings ====================
$("#SettingsBtn").click(function () {
    loadSettings();
});
function setTheme(color) {

    const themes = {
        blue:   { r: 25,  g: 0,   b: 255 },
        red:    { r: 255, g: 0,   b: 0   },
        orange: { r: 255, g: 140, b: 0   },
        pink:   { r: 255, g: 20,  b: 147 }
    };

    const theme = themes[color];
    if (!theme) return;

    const root = document.documentElement.style;

    root.setProperty('--theme-r', theme.r);
    root.setProperty('--theme-g', theme.g);
    root.setProperty('--theme-b', theme.b);
}
eel.expose(setTheme);
document.addEventListener("DOMContentLoaded", function () {
    setTheme("blue");
});

});